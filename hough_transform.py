import cv2 as cv
import numpy as np


if __name__ =='__main__':



    img = cv.imread('eye3.jpg', cv.IMREAD_GRAYSCALE)


    def nothing(*arg):
        pass


    cv.namedWindow('trackbars')
    #cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", 0, 100, nothing)
    cv.createTrackbar("Sigma", "trackbars", 0, 100, nothing)
    cv.createTrackbar("Min", "trackbars", 0, 500, nothing)
    cv.createTrackbar("Max", "trackbars", 0, 500, nothing)
    cv.createTrackbar("acc", "trackbars", 15, 30, nothing)
    cv.createTrackbar("Mindist", "trackbars", 70, 200, nothing)
    cv.createTrackbar("p1", "trackbars", 50, 200, nothing)
    cv.createTrackbar("p2", "trackbars", 70, 200, nothing)
    cv.createTrackbar("r1", "trackbars", 10, 200, nothing)
    cv.createTrackbar("r2", "trackbars", 25, 200, nothing)

    while (True):
        img = cv.imread('eye3.jpg', cv.IMREAD_GRAYSCALE)
        jadro = cv.getTrackbarPos("Jadro", "trackbars") * 2 + 1
        sigma = cv.getTrackbarPos("Sigma", "trackbars") / 10
        min = cv.getTrackbarPos("Min", "trackbars")
        max = cv.getTrackbarPos("Max", "trackbars")
        acc = cv.getTrackbarPos("acc", "trackbars") / 10
        mindist = cv.getTrackbarPos("Mindist", "trackbars")
        p1=cv.getTrackbarPos("p1", "trackbars")
        p2=cv.getTrackbarPos("p2", "trackbars")
        r1=cv.getTrackbarPos("r1", "trackbars")
        r2=cv.getTrackbarPos("r2", "trackbars")
        blur_img = cv.GaussianBlur(img, (jadro, jadro), sigma)
        edges = cv.Canny(blur_img, min, max)
        cv.imshow("edges", edges)
        circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, acc, mindist)
        cimg = cv.imread('eye3.jpg')
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv.circle(cimg, (x, y), r, (0, 255, 0), 2)
               # cv.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        # for i in circles[0, :]:
        #     # draw the outer circle
        #     cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        #     # draw the center of the circle
        #     cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


        cv.imshow("img", cimg)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break