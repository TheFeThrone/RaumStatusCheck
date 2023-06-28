import cv2
import cascade_loaders


face_cascade = cascade_loaders.load_face_cascade()
profile_cascade = cascade_loaders.load_profile_cascade()


def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


def detect_profiles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    profiles = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return profiles
