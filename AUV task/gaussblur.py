import cv2
import imutils
import numpy as np
#image reading
image = cv2.imread('simple.jpg')
dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(imgray,9,75,75)
ret,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(image,kernel,iterations = 1)
dilation = cv2.dilate(image,kernel,iterations = 1)


#finding contours in the images which will then help us in finding the centre coordinate
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# loop over the contours
for c in contours:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
 
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, c, -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
   #print cx
    #print cy
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

