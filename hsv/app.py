import time
import edgeiq
import cv2
"""
Value channel view from a Lepton camera
"""


def main():

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=1) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            # loop detection
            while True:
                frame = video_stream.read()

                # HSV
                frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
                frame_value = frame_hsv[:, :, 2]

                # Generate text to display on streamer
                text = "Lepton HSV - Value Channel Image"

                streamer.send_data(frame_value, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
