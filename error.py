import cv2
import numpy as np

if __name__ == "__main__":
	img = cv2.imread('test.jpg')
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower_range = np.array([0, 100, 100], dtype=np.uint8)
	upper_range = np.array([15, 255, 255], dtype=np.uint8)

	mask = cv2.inRange(hsv, lower_range, upper_range)

	edges = cv2.Canny(mask,50,150,apertureSize = 3)

	lines = cv2.HoughLines(edges,1,np.pi/180,1000)
	for line in lines:
	    a = np.cos(line[0][1])
	    b = np.sin(line[0][1])
	    x0 = a*line[0][0]
	    y0 = b*line[0][0]
	    x1 = int(x0 + 100000*(-b))
	    y1 = int(y0 + 100000*(a))
	    x2 = int(x0 - 100000*(-b))
	    y2 = int(y0 - 100000*(a))
	    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

	cv2.imwrite('result.jpg',img)

