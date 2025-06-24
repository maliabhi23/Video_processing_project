import cv2
import numpy as np

def compute_feature_vector(image_path: str) -> list:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image could not be loaded: {image_path}")

    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist.tolist()
