# 🎓 Smart Classroom AI System

Smart Classroom AI is an **advanced real-time AI-powered classroom monitoring system** built using **Python, OpenCV, Deep Learning, and Streamlit**.  
The system automatically analyzes classroom activities using a live camera feed and provides intelligent insights, alerts, and analytics.

This project focuses on **practical, real-world classroom automation**, not just theory.

## 🚀 Project Overview

Smart Classroom AI assists teachers and institutions by:

- Automatically marking attendance
- Monitoring student engagement
- Detecting inattentiveness, drowsiness, phone usage, and abnormal behavior
- Generating real-time alerts
- Showing live analytics on a dashboard

The system works completely in **real time** using a webcam or CCTV feed.

## 🎯 Objectives

- Reduce manual attendance effort
- Improve classroom engagement monitoring
- Detect unsafe or abnormal behavior early
- Provide real-time decision support to teachers
- Build an industry-level AI system using computer vision

## 🧠 Features Implemented

### ✅ Attendance & Identity
- Face Recognition based Attendance
- Duplicate attendance prevention
- Late entry detection
- Unknown person detection

### 😊 Emotion & Engagement Analysis
- Emotion detection (Happy, Neutral, Sad, Angry, Fear, etc.)
- Engagement score calculation
- Dominant emotion identification
- Session-wise emotion analytics

### 👀 Attention Monitoring
- Focused vs Not Focused detection
- Class-level attention statistics

### 😴 Drowsiness Detection
- Awake / Drowsy / Sleeping state detection
- Smart alert control (no repeated alert spam)

### 📱 Phone Usage Detection
- Detects mobile phone usage in classroom
- Real-time alert generation

### ⚠️ Violence & Risk Detection
- Detects violent activity patterns
- Classroom risk level classification (LOW / MEDIUM / HIGH)

### 🚨 Intelligent Alert System
- Unknown face alerts
- Negative emotion alerts
- Low engagement alerts
- Drowsiness alerts
- Phone usage alerts
- Risk level alerts
- All alerts logged with timestamps

### 📊 Live Dashboard (Streamlit)
- Faces detected
- Recognized vs unknown students
- Recent emotions
- Attention statistics
- Phone usage status
- Live classroom analytics



## 🗂️ Project Folder Structure

```
Smart_Classroom_AI/
│
├── attendance/
│   ├── mark_attendance.py
│   └── attendance_logic.py
│
├── analytics/
│   └── emotion_analytics.py
│
├── alerts/
│   └── alert_manager.py
│
├── attention/
│   └── attention_detector.py
│
├── camera.py
├── config/
│   └── class_time.py
├── dashboard/
│   └── app.py
├── drowsiness/
│   └── drowsiness_detector.py
│
├── phone/
│   └── phone_detector.py
│
├── violence/
│   └── violence_detector.py
│
├── models/
│   ├── face_model.yml
│   ├── emotion_model.h5
│   ├── labels.pkl
│   └── yolov5s.pt
│
├── reports/
│   ├── session_summary.txt
│   ├── late_entries.txt
│   └── alerts_log.txt
│
├── runtime/
│   ├── live_data.json
│   └── live_data_temp.json
├── recognize.py
├── run_all.py
├── train_emotion.py
├── train_face.py
├── requirements.txt
```

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **OpenCV** - Computer vision processing
- **TensorFlow / Keras** - Deep learning framework
- **NumPy** - Numerical computing
- **YOLO** - Object detection system
- **Streamlit** - Interactive dashboards
- **Flask** - Web framework for integration
- **Computer Vision** - Image processing techniques
- **Deep Learning** - Neural networks for recognition

## ▶️ How to Run the Project

### Method 1: Traditional Approach
```bash
# Windows
venv\Scripts\activate

# Start recognition system
python recognize.py

# In another terminal, start dashboard
streamlit run dashboard/app.py
```

### Method 2: Web Interface (Enhanced)
```bash
# Install requirements
pip install flask

# Start the integrated web server
python proper_camera_server.py

# Access at http://localhost:8080
```

### Method 3: All-in-One
```bash
# Run the integrated system
python start_web_ai.py
```

## 📈 Output Generated

- Live webcam window with:
  - Student name
  - Emotion
  - Attention status
  - Drowsiness state
  - Terminal alerts in real time
  - Session summary report
  - Alerts log file
- Live dashboard with classroom analytics
- Web interface with real-time camera feed and controls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
