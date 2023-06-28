import cv2

def load_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def load_profile_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
