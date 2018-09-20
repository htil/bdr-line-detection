import cv2
import numpy as np

if __name__ == "__main__":
	img = cv2.imread('test.jpg')
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower_range = np.array([0, 100, 100], dtype=np.uint8)
	upper_range = np.array([15, 255, 255], dtype=np.uint8)

	mask = cv2.inRange(hsv, lower_range, upper_range)

	edges = cv2.Canny(mask,50,150,apertureSize = 3)
	cv2.imwrite('mask.jpg',mask)
	cv2.imwrite('edges.jpg', edges)
