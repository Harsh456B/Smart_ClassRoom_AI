import cv2

class Camera:
    def __init__(self):
        # Webcam start
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise RuntimeError("Camera not accessible")

    def read(self):
        # Camera se frame read karo
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def close(self):
        # Camera band karo
        self.cap.release()
        cv2.destroyAllWindows()
