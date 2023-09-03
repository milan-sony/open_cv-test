import cv2
import numpy as np

# capture video from camera
"""
To capture a video, you need to create a VideoCapture object. Its argument can be either the device index or the name of a video file
eg: cv2.VideoCapture(0) or cv2.VideoCapture("filename.extension")
"""

# creats a VideoCapture object
cap = cv2.VideoCapture(0)

# if there is no video or camera does'nt open up it will print the message
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# we are creating an infinte loop to capture the video infinite
"""
cap.read() returns two values one is the image/frame which is a numpy array and another is  a boolean value  (True/False). If the frame is read correctly, it will be True else False
"""

while True:
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame.")
        break

    """
    Note: In OpenCV the color is in BGR (BLUE, GREEN, RED) format
    """

    # draw a diagonal line
    """
    Blue line with thickness of 5 px
    (image, starting point, end point, color, thickness)
    """
    cv2.line(frame,(0,0),(511,511),(255,0,0),5)

    # draw rectangle
    """
    To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
    Drawing a green rectangle at the top-right corner of image.
    """
    cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)

    # draw circle
    """
        To draw a circle, you need its center coordinates and radius. 
        Here we will draw a circle inside the rectangle drawn above , -1 for filled circle.
    """
    cv2.circle(frame,(447,63), 63, (0,0,255), 4)
    
    # draw polygon
    """
    To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32. 
    Here we draw a small polygon of with four vertices in yellow color.
    """
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(frame,[pts],True,(0,255,255))

    # adding text
    """
    To put texts in images, you need specify following things.
        Text data that you want to write
        Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
        Font type (Check cv.putText() docs for supported fonts)
        Font Scale (specifies the size of font)
        regular things like color, thickness, lineType etc.
        For better look, lineType = cv.LINE_AA is recommended.
    """
    # (frame, text, position, font, size/scale, color, thickness, cv2.LINE_AA)
    # cv2.LINE_AA is the line type
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'OpenCV Test',  (10,300), font,  2, (255,255,255), 2, cv2.LINE_AA)

    # display the frame
    cv2.imshow("Frame", frame)

    # it will wait for 1 millisecond to capture next frame and also  if the key q is pressed it will stop
    if cv2.waitKey(1) == ord('q'):
        break

# releasing the capture when everything is done
cap.release()
cv2.destroyAllWindows()