import cv2

def initialize_video_capture():
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use 0 for the default camera, or specify the camera index #
    # Set camera properties for optimal performance #
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280/2)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720/2)
    return video_capture

def release_video_capture(video_capture):
    video_capture.release()

def display_frame(frame):
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True  # Return True to indicate that the loop should exit #
    return False
