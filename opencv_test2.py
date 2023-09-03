import cv2

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

    # frame resize
    resized_frame = cv2.resize(frame, (600,400))
    
    # display the frame
    cv2.imshow("Frame", resized_frame)

    # it will wait for 1 millisecond to capture next frame and also  if the key q is pressed it will stop
    if cv2.waitKey(1) == ord('q'):
        break

# releasing the capture when everything is done
cap.release()
cv2.destroyAllWindows()