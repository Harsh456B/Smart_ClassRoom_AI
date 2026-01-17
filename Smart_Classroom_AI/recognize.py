import cv2
import pickle
import numpy as np
import json
import os

from tensorflow.keras.models import load_model
from attendance.mark_attendance import mark_attendance
from attendance.attendance_logic import should_mark_attendance
from config.class_time import is_late
from camera import Camera
from alerts.alert_manager import AlertManager
from attention.attention_detector import detect_attention
from drowsiness.drowsiness_detector import DrowsinessDetector
from phone.phone_detector import detect_phone
from violence.violence_detector import ViolenceDetector  


# ----------------------------
# INITIALIZE HELPERS
# ----------------------------
camera = Camera()
alert = AlertManager()
drowsiness_detector = DrowsinessDetector()
violence_detector = ViolenceDetector()   

THRESHOLD = 200
recognized_count = 0
unknown_count = 0
emotion_log = []

os.makedirs("reports", exist_ok=True)
os.makedirs("runtime", exist_ok=True)

# ----------------------------
# LOAD MODELS
# ----------------------------
emotion_model = load_model("models/emotion_model.h5")
emotion_labels = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprise"]

face_model = cv2.face.LBPHFaceRecognizer_create()
face_model.read("models/face_model.yml")

with open("models/labels.pkl","rb") as f:
    labels = pickle.load(f)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ----------------------------
# MAIN LOOP
# ----------------------------
try:
    while True:

        frame = camera.read()
        if frame is None:
            continue

        frame_h, frame_w = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # ---------------- PHONE DETECTION ----------------
        phone_detected = detect_phone(frame)
        if phone_detected:
            alert.phone_alert()
            cv2.putText(frame,"PHONE DETECTED!",
                        (20,70),cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,(0,0,255),3)

        # ---------------- VIOLENCE DETECTION (PHASE 7) ----------------
        violent = violence_detector.detect(frame)
        if violent:
            alert.violence_alert()
            cv2.putText(
                frame,"VIOLENCE DETECTED!",
                (20,110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0,0,255),
                3
            )

        # Faces count
        cv2.putText(frame,f"Faces Detected: {len(faces)}",
                    (20,30),cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,(255,255,0),2)

        current_recognized = []
        current_unknown = 0
        current_emotions = []
        focused_count = 0
        not_focused_count = 0

        for (x,y,w,h) in faces:

            roi = gray[y:y+h, x:x+w]
            roi = cv2.resize(roi,(200,200))

            # ---------- EMOTION ----------
            emo = cv2.resize(roi,(48,48))/255.0
            emo = emo.reshape(1,48,48,1)
            emotion = emotion_labels[np.argmax(emotion_model.predict(emo,verbose=0))]

            emotion_log.append(emotion)
            current_emotions.append(emotion)

            if emotion in ["Angry","Sad","Fear"]:
                alert.negative_emotion_alert(emotion)

            # ---------- ATTENTION ----------
            attention = detect_attention(x,y,w,h,frame_w,frame_h)
            attentive = attention == "Focused"

            focused_count += attentive
            not_focused_count += not attentive

            # ---------- DROWSINESS ----------
            sleep_state = drowsiness_detector.update(attentive, emotion)
            if sleep_state in ["Drowsy","Sleeping"]:
                alert.drowsiness_alert(sleep_state)

            # ---------- FACE RECOGNITION ----------
            label_id, conf = face_model.predict(roi)

            if conf < THRESHOLD:
                name = labels[label_id]
                current_recognized.append(name)
                color = (0,255,0)

                if should_mark_attendance(name):
                    mark_attendance(name)
                    recognized_count += 1
                    if is_late():
                        with open("reports/late_entries.txt","a") as f:
                            f.write(f"{name} - Late Entry\n")

                text = f"{name} | {int(conf)}"
                status = "Attendance: Marked"

            else:
                name = "Unknown"
                current_unknown += 1
                unknown_count += 1
                color = (0,0,255)
                text = "Unknown"
                status = "Attendance: Not Allowed"
                alert.unknown_alert()

            # ---------- DISPLAY ----------
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            cv2.putText(frame,text,(x,y-35),
                        cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
            cv2.putText(frame,status,(x,y-15),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)
            cv2.putText(frame,f"Emotion: {emotion}",
                        (x,y+h+25),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,color,2)
            cv2.putText(frame,f"Attention: {attention}",
                        (x,y+h+45),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
            cv2.putText(frame,f"State: {sleep_state}",
                        (x,y+h+65),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,
                        (0,255,0) if sleep_state=="Awake" else (0,0,255),2)

        # ---------------- LIVE DATA ----------------
        live_data = {
            "faces_detected": len(faces),
            "recognized_faces": len(current_recognized),
            "unknown_faces": current_unknown,
            "recent_emotions": current_emotions[-5:],
            "focused": focused_count,
            "not_focused": not_focused_count,
            "phone_detected": phone_detected,
            "violence_detected": violent
        }

        with open("runtime/live_data.json","w") as f:
            json.dump(live_data,f)

        cv2.imshow("Smart Classroom AI", frame)
        cv2.waitKey(1)

        if cv2.getWindowProperty("Smart Classroom AI",cv2.WND_PROP_VISIBLE) < 1:
            break

except KeyboardInterrupt:
    print("\nCTRL+C Exit")

finally:
    camera.close()
    print("\nSession Summary")
    print("Recognized:",recognized_count)
    print("Unknown:",unknown_count)

    from analytics.emotion_analytics import analyze_emotions
    result = analyze_emotions(emotion_log)

    if result:
        score = result["engagement_score"]
        if score < 40:
            alert.low_engagement_alert(score)
        alert.risk_level_alert("HIGH" if score<30 else "MEDIUM" if score<60 else "LOW")
