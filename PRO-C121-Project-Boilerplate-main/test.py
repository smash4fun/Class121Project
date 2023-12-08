import cv2
import time

#Helps to calculations within arrays
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('MountEverest.jpg')

# resizing the mountain image as 640 X 480

mountain.resize(640,480)

#Allowing the webcam to start by making the code sleep for 2 seconds
bg = 0

#Capturing background for 60 frames and storing in bg and ret
#ret (dummy variable) contains 0 or 1 to check if code words
for i in range(60):
    ret, bg = camera.read()
#Flipping the background
bg = np.flip(bg, axis=1)

#While video is open, captutre the frames
while (camera.isOpened()):
    ret, img = camera.read()
    #if isn't working, stop the loop
    if ret==0:
        break

    #Flipping the image of us
    img = np.flip(mountain, axis=1)

    #Converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Generating mask to detect red colour(values can be changed)
    #rangeStart = np.array([huestart, saturationstart, valuestart])
    #rangeEnd = np.array([hueend, saturationend, valueend])
    #variable = cv2.inRange(hsv, rangeStart, rangeEnd)
    #Takes the range between values in rangeStart and rangeEnd

    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([360, 255, 2])

    cv2.imshow("mask_1", mask_1)

    #Open and expand the image where there is mask 1 (color)
    #Wherever there is red, there is now white
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    #Selecting only the part that does not have mask one and saving in mask 2
    #Taking the parts that are not red into mask_2
    mask_2 = cv2.bitwise_not(mask_1)

    #Keeping our image(running image) without red color into mask_2
    res_1 = cv2.bitwise_and(img,img, mask=mask_2)
   

    #Keeping only the part of the images with the red color into mask_1
    res_2 = cv2.bitwise_and(bg,bg, mask=mask_1)

    #Generating the final output by merging res_1 and res_2
    #cv2.addWeighted(image1, alpha(transparency of image 1), image2, beta alpha(transparency of image 2), gamma)
    final_output = cv2.addWeighted(res_1, 1, res_2, 1,0)
        
    #Displaying the output to the user
    cv2.imshow("Magic", final_output)
    cv2.waitKey(1)

#Releasing the vid and destroying it
camera.release()
cv2.destroyAllWindows()


