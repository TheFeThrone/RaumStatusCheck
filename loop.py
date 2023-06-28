import time
import detection
import draw
import camera


def run_main_loop(video_capture):
    empty_duration = 60  # Duration in seconds to consider it as "empty"
    start_time = time.time()

    while True:
        # Read the current frame from the video capture
        ret, frame = video_capture.read()

        # Detect faces and profiles
        faces = detection.detect_faces(frame)
        profiles = detection.detect_profiles(frame)

        # Draw rectangles around the detected faces and profiles
        draw.draw_rectangles(frame, faces, (0, 255, 0))  # Draw rectangles around faces
        draw.draw_rectangles(frame, profiles, (255, 0, 0))  # Draw rectangles around profiles

        # Display the resulting frame
        should_exit = camera.display_frame(frame)
        if should_exit:
            break

        # Check if any detections are made
        if len(faces) > 0 or len(profiles) > 0:
            start_time = time.time()  # Reset the start time

        # Check if no detections for the specified duration
        elapsed_time = time.time() - start_time
        if elapsed_time >= empty_duration:
            print("Empty")
            start_time = time.time()
