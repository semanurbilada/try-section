# =============================================== THEORY =======================================================
# This script attempts to stream real-time video with YOLO object detection results using the pyshine library.
# The script captures video from the camera, performs object detection using the YOLO model, and then streams
# the annotated video frames over the network using pyshine.
#
# The pyshine library is designed for simple video streaming applications. However, integrating it with real-time 
# image processing (like YOLO object detection) can be challenging due to the additional computational load and 
# synchronization requirements.
# ===============================================================================================================
import cv2
import time
import logging
from style import HTML
from ultralytics import YOLO
import pyshine as ps  # pip3 install pyshine==0.0.9

def main(server_ip='172.20.10.2', port=9000):
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = (server_ip, port)

    model = YOLO('weights_path')
    prev_time = time.time()
    width, height = 640, 480
    font = cv2.FONT_HERSHEY_SIMPLEX

    logging.getLogger('ultralytics').setLevel(logging.WARNING)

    try:
        StreamProps.set_Mode(StreamProps, 'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        capture.set(cv2.CAP_PROP_FPS, 30)

        StreamProps.set_Capture(StreamProps, capture)
        StreamProps.set_Quality(StreamProps, 90)

        server = ps.Streamer(address, StreamProps)
        print('Server started at', 'http://' + address[0] + ':' + str(address[1]))

        while capture.isOpened():
            success, frame = capture.read()

            if success:
                frame = cv2.resize(frame, (width, height))

                # fps calculation
                current_time = time.time()
                fps = 1 / (current_time - prev_time)
                prev_time = current_time

                # predict results
                result = model.predict(source=frame, conf=0.6)
                annotated_frame = result[0].plot()
                
                # overlay FPS on the frame
                cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 20), font, 0.5, (0, 255, 0), 2)
                cv2.imshow("YOLOv8 Detection", annotated_frame)

                # press ESC to exit
                if cv2.waitKey(1) & 0xFF == 27:
                    break

                # update the frame to be streamed
                StreamProps.frame = annotated_frame

            else:
                print("\nNo frame from camera!\n")
                break

        server.serve_forever()

    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'capture' in locals():
            capture.release()
        if 'server' in locals():
            server.socket.close()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()