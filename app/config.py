import os

FRAME_OUTPUT_DIR = "extracted_frames"
FRAME_INTERVAL_SECONDS = 1
QDRANT_COLLECTION = "video_frames"

os.makedirs(FRAME_OUTPUT_DIR, exist_ok=True)
