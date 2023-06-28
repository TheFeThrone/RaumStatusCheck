import cv2

def draw_rectangles(frame, detections, color):
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
