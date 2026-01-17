import os
from datetime import datetime

class AlertManager:

    def __init__(self):
        os.makedirs("reports", exist_ok=True)
        self.last_drowsy_state = None
        self.last_violence = False   # spam control

    def _log(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("ALERT:", message)

        with open("reports/alerts_log.txt", "a") as f:
            f.write(f"[{time}] {message}\n")

    def unknown_alert(self):
        self._log("Unknown face detected")

    def low_engagement_alert(self, score):
        self._log(f"Low classroom engagement detected ({score}%)")

    def negative_emotion_alert(self, emotion):
        self._log(f"Negative emotion detected: {emotion}")

    def risk_level_alert(self, level):
        self._log(f"Class Risk Level: {level}")

    def drowsiness_alert(self, state):
        if state != self.last_drowsy_state:
            self._log(f"Student drowsiness detected: {state}")
            self.last_drowsy_state = state

    def phone_alert(self):
        self._log("Mobile phone usage detected")

    def violence_alert(self):
        if not self.last_violence:
            self._log("Violence detected in classroom")
            self.last_violence = True
