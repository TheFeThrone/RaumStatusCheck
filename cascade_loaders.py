import cv2

def load_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def load_profile_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

def load_bodies_hog_descriptor():
    bodies = cv2.HOGDescriptor()
    bodies.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    return bodies

def load_upperbody_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')