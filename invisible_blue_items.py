# color differentiate
import cv2
import numpy as np
image = cv2.imread('C:/Users/SONY JOY/Documents/ty.jpg',1)
# resize
image = cv2.resize(image, (320,240))
# lower value for blue color
lower_val = np.array([94,80,2])
# higher value for blue color
higher_val = np.array([126,255,255])
# converting BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.inRange() function gives us the mask having colors within the specified lower and upper range
# things left as black color, given/provided color range removed
mask = cv2.inRange(hsv, lower_val, higher_val)
# cv2.bitwise_and() function performs logical and operation on pixels of original image and mask
result = cv2.bitwise_and(image, image, mask=mask)
# display
cv2.imshow('original', image)
cv2.imshow('hsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
