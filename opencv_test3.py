import cv2

# saving a video
cap = cv2.VideoCapture(0)

"""
Here we create a VideoWriter object. It contains the output file name (eg: output.avi). Then the FourCC code (FourCC is a 4-byte code used to specify the video codec). Then number of frames per second (fps) and frame size should be passed. And the last one is the isColor flag. If it is True, the encoder expect color frame, otherwise it works with grayscale frame.
"""

# define the codec and create VideoWriter object
# FourCC code is passed as `cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG')` for MJPG.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# we are creating an infinte loop to capture the video infinite
"""
cap.read() returns two values one is the image/frame which is a numpy array and another is  a boolean value  (True/False). If the frame is read correctly, it will be True else False
"""

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame")
        break

    #  flips every frame in the vertical direction (0 - inverted)
    # frame = cv2.flip(frame, 1)

    # writing the frame
    out.write(frame)

    # imshow() display the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()