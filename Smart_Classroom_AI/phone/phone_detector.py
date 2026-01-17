from ultralytics import YOLO

# Load YOLO model only once
model = YOLO("models/yolov5s.pt")

def detect_phone(frame):
    """
    Detects mobile phone in a frame
    Returns True if phone detected else False
    """

    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]

            if label == "cell phone":
                return True

    return False
