import cv2
import numpy as np

class ViolenceDetector:
    def __init__(self):
        self.prev_gray = None
        self.motion_counter = 0

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return False

        frame_delta = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        motion_area = cv2.countNonZero(thresh)
        self.prev_gray = gray

        # 🔥 TUNED FOR CLASSROOM
        if motion_area > 15000:
            self.motion_counter += 1
        else:
            self.motion_counter = 0

        # 5 continuous high-motion frames = violence
        if self.motion_counter >= 5:
            self.motion_counter = 0
            return True

        return False
