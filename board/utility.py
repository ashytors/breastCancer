#validasi file
import cv2
import numpy as np

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Image at {img_path} couldn't be loaded.")
    img = cv2.resize(img, (50,50), interpolation=cv2.INTER_LINEAR)
    img = np.expand_dims(img, axis=0)
    
    return img
