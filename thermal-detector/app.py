import time
import edgeiq
import cv2
import numpy as np
"""
thermal detector using a Lepton FLiR camera 
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
                frame_value = frame_hsv[:,:,2]

                # bilateral filter - edge-preserving image smoothing method
                blurredBrightness = cv2.bilateralFilter(frame_value, 9, 150, 150)

                # Canny edge detector
                thresh = 50
                edges = cv2.Canny(blurredBrightness,thresh,thresh*2, L2gradient=True)

                # create a binary image by thresholding the original image and
                # putting a 1 wherever the pixel is warm, and a 0 where it’s not
                _,mask = cv2.threshold(blurredBrightness,200,1,cv2.THRESH_BINARY)

                # erode away at the blobs of 1’s created by that operation
                erodeSize = 5
                eroded = cv2.erode(mask, np.ones((erodeSize, erodeSize)))

                # expand those blobs again to be roughly the same size as before
                dilateSize = 7
                mask = cv2.dilate(eroded, np.ones((dilateSize, dilateSize)))

                # Generate text to display on streamer
                text = "Thermal Detector"

                streamer.send_data((cv2.resize(cv2.cvtColor(mask*edges, cv2.COLOR_GRAY2RGB)
                    | frame, (640, 480), interpolation = cv2.INTER_CUBIC)), text)

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
