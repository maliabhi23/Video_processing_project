import cv2
import os
import uuid
from app.config import FRAME_INTERVAL_SECONDS, FRAME_OUTPUT_DIR

def extract_frames(video_path: str) -> list:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * FRAME_INTERVAL_SECONDS)

    saved_frames = []
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % interval == 0:
            filename = f"{uuid.uuid4().hex}.jpg"
            filepath = os.path.join(FRAME_OUTPUT_DIR, filename)
            cv2.imwrite(filepath, frame)
            saved_frames.append(filepath)
        i += 1
    cap.release()
    return saved_frames
