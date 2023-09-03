# import open cv
import cv2

# load image
# imread("path to the image, mode to load the image")
"""
Different modes
---------------------------
cv2.IMREAD_COLOR or -1      : Loads the color image. It's the default flag 
cv2.IMREAD_GRAYSCALE or 0   : Loads the img in grayscale
cv2.IMREAD_UNCHANGED or 1   : Loads the img with alpha channel

mode is not necessary unless you want the image to appeare in grayscale and all
"""

# you can give differnt variable names for each one
img = cv2.imread("./assets/dog.jp")

# if there is no image it will print the messsage
if img is None:
    print("Could not read the image.")

# resize the image
img = cv2.resize(img, (400,400))

# rotate the image
img = cv2.rotate(img, cv2.ROTATE_180)

# save the image
cv2.imwrite("new_img.jpg", img)

# display image
cv2.imshow("Window Name", img)

# close the window
# waitKey(0) means it will wait for infinite amount of time until any key is pressed
# if waitKey(4) it will wait for 4 sec then close automatically
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()