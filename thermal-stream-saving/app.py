import time
import edgeiq
"""
Save Lepton thermal camera video stream
"""


def main():
    filename = "thermal-stream.avi"

    fps = edgeiq.FPS()
    writer = edgeiq.VideoWriter(filename)
    print(filename)

    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            # loop detection
            while True:
                frame = video_stream.read()

                # Generate text to display on streamer
                text = "FLiR Lepton"
                writer.write_frame(frame)

                streamer.send_data(frame, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        writer.close()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
