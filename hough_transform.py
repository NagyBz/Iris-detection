import cv2 as cv
import numpy as np


if __name__ =='__main__':



    img = cv.imread('eye1.jpg', cv.IMREAD_GRAYSCALE)


    def nothing(*arg):
        pass


    cv.namedWindow('trackbars')
    cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", 0, 100, nothing)
    cv.createTrackbar("Sigma", "trackbars", 0, 100, nothing)
    cv.createTrackbar("Min", "trackbars", 0, 500, nothing)
    cv.createTrackbar("Max", "trackbars", 0, 500, nothing)
    cv.createTrackbar("p1", "trackbars", 50, 200, nothing)
    cv.createTrackbar("p2", "trackbars", 70, 200, nothing)
    cv.createTrackbar("r1", "trackbars", 10, 200, nothing)
    cv.createTrackbar("r2", "trackbars", 25, 200, nothing)

    while (True):
        jadro = cv.getTrackbarPos("Jadro", "trackbars")
        sigma = cv.getTrackbarPos("Sigma", "trackbars")
        min = cv.getTrackbarPos("Min", "trackbars")
        max = cv.getTrackbarPos("Max", "trackbars")
        p1=cv.getTrackbarPos("p1", "trackbars")
        p2=cv.getTrackbarPos("p2", "trackbars")
        r1=cv.getTrackbarPos("r1", "trackbars")
        r2=cv.getTrackbarPos("r2", "trackbars")
        blur_img = cv.GaussianBlur(img, (5, 5), 50, 5)
        edges = cv.Canny(blur_img, 120, 100)

        circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1.3, 100)

        for i in circles[0, :]:
            # draw the outer circle
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


        cv.imshow("trackbars", img)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break