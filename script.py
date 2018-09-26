from LineError import *
import time

if __name__ == '__main__':
    le = LineError(1)
    l = cv2.imread('left.jpg')

    delta, theta = le.GetError(l)
    print(delta, theta)

    cv2.imwrite("result.jpg", le.GetImage())
