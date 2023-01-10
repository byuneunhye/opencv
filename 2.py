import cv2

img = cv2.imread('data/Dog.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', gray)
cv2.waitKey()
cv2.destroyAllWindows()