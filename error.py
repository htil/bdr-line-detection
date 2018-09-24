import cv2
import numpy as np
from math import sqrt

if __name__ == "__main__":
    image = cv2.imread('test2.jpg')
    blur = cv2.blur(image,(20,20))
    hls = cv2.cvtColor(blur, cv2.COLOR_RGB2HLS)

    # apply red color mask
    lower_range = np.array([50, 50, 100], dtype=np.uint8)
    upper_range = np.array([255, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hls, lower_range, upper_range)

    masked_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite('mask.jpg', masked_image)

    # apply canny edge detection
    edges = cv2.Canny(masked_image,50,150,apertureSize = 3)
    cv2.imwrite('edges.jpg', edges)

    lines = cv2.HoughLines(edges,1,np.pi/180,500)

    x1v = []
    x2v = []
    angles = []

    h, w = image.shape[:2]
    print(h, w)

    for line in lines[:2]:
        a = np.cos(line[0][1])
        b = np.sin(line[0][1])
        x0 = a*line[0][0]
        y0 = b*line[0][0]

        x1 = int(x0 + 100000*(-b))
        y1 = int(y0 + 100000*(a))
        x2 = int(x0 - 100000*(-b))
        y2 = int(y0 - 100000*(a))

        dist = abs((y2-y1)*(w/2) - (x2-x1)*(h/2) + x2*y1 - y2*x1)/sqrt((y2-y1)**2 + (x2-x1)**2)
        print("dist is " + str(dist))

        x1v.append(x1)
        x2v.append(x2)
        angles.append(line[0][1])

        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)


    x1_avg = sum(x1v)//len(x1v)
    x2_avg = sum(x2v)//len(x2v)
    theta = sum(angles)/len(angles)



    print(x1_avg, x2_avg, theta)

    cv2.imwrite('result.jpg',image)
