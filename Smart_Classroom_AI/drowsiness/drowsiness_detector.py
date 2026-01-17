import time

class DrowsinessDetector:
    def __init__(self):
        self.start_time = None
        self.state = "Awake"

    def update(self, attentive: bool, emotion: str):
        current_time = time.time()

        # 🔥 UPDATED CONDITION
        if emotion in ["Sad", "Neutral", "Fear"]:

            if self.start_time is None:
                self.start_time = current_time

            elapsed = current_time - self.start_time

            if elapsed > 6:
                self.state = "Sleeping"
            elif elapsed > 3:
                self.state = "Drowsy"
            else:
                self.state = "Blinking"

        else:
            self.start_time = None
            self.state = "Awake"

        return self.state
