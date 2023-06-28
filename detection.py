import cv2
import cascade_loaders

face_cascade = cascade_loaders.load_face_cascade()
profile_cascade = cascade_loaders.load_profile_cascade()
body_hog = cascade_loaders.load_bodies_hog_descriptor()
upperbody_cascade = cascade_loaders.load_upperbody_cascade()

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def detect_profiles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    profiles = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return profiles

def detect_bodies_hog(frame):
    bodies, _ = body_hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    return bodies

def detect_upper_bodies(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    upper_bodies = upperbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return upper_bodies