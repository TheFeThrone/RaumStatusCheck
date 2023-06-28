import cv2
import camera
import loop


def main():
    # Initialize the video capture #
    video_capture = camera.initialize_video_capture()

    # Run the main loop #
    loop.run_main_loop(video_capture)

    # Release the video capture and close the window #
    camera.release_video_capture(video_capture)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
