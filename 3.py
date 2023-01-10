
import cv2

img = cv2.imread('data/Dog.jpg')

cv2.imshow('image', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()