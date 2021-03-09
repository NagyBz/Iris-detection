# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':

    img = cv.imread('eye1.jpg', cv.IMREAD_GRAYSCALE)


    def nothing(*arg):
        pass


    cv.namedWindow('trackbars')
    cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", 5, 10, nothing)
    cv.createTrackbar("Sigma", "trackbars", 34, 50, nothing)
    cv.createTrackbar("LowTreshold", "trackbars", 33, 200, nothing)
    cv.createTrackbar("HighTreshold", "trackbars", 90, 200, nothing)

    while (True):
        jadro = cv.getTrackbarPos("Jadro", "trackbars") * 2 + 1
        sigma = cv.getTrackbarPos("Sigma", "trackbars") / 10
        lowT = cv.getTrackbarPos("LowTreshold", "trackbars")
        highT= cv.getTrackbarPos("HighTreshold", "trackbars")

        blur_img = cv.GaussianBlur(img, (jadro, jadro), sigma)
        edges = cv.Canny(blur_img, lowT, highT)

        cv.imshow("trackbars", edges)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break
