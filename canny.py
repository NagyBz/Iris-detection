
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


if __name__ =='__main__':
    img=cv.imread('eye1.jpg',cv.IMREAD_GRAYSCALE)

    def nothing(*arg):
        pass
    cv.namedWindow('trackbars')
    cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", 0, 100, nothing)
    cv.createTrackbar("Sigma", "trackbars", 0, 30, nothing)
    cv.createTrackbar("Min", "trackbars", 0, 500, nothing)
    cv.createTrackbar("Max", "trackbars", 0, 500, nothing)

    while (True):
        jadro = cv.getTrackbarPos("Jadro", "trackbars") * 2 + 1
        sigma = cv.getTrackbarPos("Sigma", "trackbars") / 10
        min =cv.getTrackbarPos("Min", "trackbars")
        max= cv.getTrackbarPos("Max", "trackbars")
        blur_img = cv.GaussianBlur(img, (jadro, jadro), sigma)
        edges = cv.Canny(blur_img, min, max)

        cv.imshow("trackbars", edges)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break