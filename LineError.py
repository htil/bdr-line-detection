import cv2
import numpy as np
from math import sqrt

class LineError(image):
    def __init__(self, image, debug = 0):
        self.delta = None
        self.theta = None
        self.image = image
        self.debug = debug

    def CalcError(self):
        # apply a Gaussian blur and convert to an HLS image
        blur = cv2.blur(self.image,(20,20))
        hls  = cv2.cvtColor(blur, cv2.COLOR_RGB2HLS)

        # apply a color filter
        lower_range = np.array([50, 50, 100], dtype=np.uint8)
        upper_range = np.array([255, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hls, lower_range, upper_range)
        masked_image = cv2.bitwise_and(self.image, self.image, mask=mask)

        # apply Canny Edge Detection
        edges = cv2.Canny(masked_image, 50, 150, apertureSize = 3)

        # apply Hough Lines algorithm
        lines = cv2.HoughLines(edges, 1, np.pi/180, 500)

        # definitions
        h, w = self.image.shape[:2]
        angles = []

        # parse results for the two most prominent lines
        for line in lines[:2]:
            a = np.cos(line[0][1])
            b = np.sin(line[0][1])
            x0 = a*line[0][0]
            y0 = b*line[0][0]

            x1 = int(x0 + 100000*(-b))
            y1 = int(y0 + 100000*(a))
            x2 = int(x0 - 100000*(-b))
            y2 = int(y0 - 100000*(a))

            num = abs((y2-y1)*(w/2) - (x2-x1)*(h/2) + x2*y1 - y2*x1)
            denom = sqrt((y2-y1)**2 + (x2-x1)**2)

            if(self.debug == 1):
                cv2.line(self.image,(x1,y1),(x2,y2),(0,255,0),5)

            angles.append(line[0][1])
            self.delta = num/denom

        # calculate the value of theta
        self.theta = sum(angles)/len(angles)

    def GetError(self):
        self.CalcError()
        return [self.delta, self.theta]
