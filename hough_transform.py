import cv2 as cv
import numpy as np
from intersection_over_union import union_area, intersection_area

if __name__ == '__main__':

    img_name = 'eye1.jpg'
    dx, dy, dr = 0, 0, 0
    zx, zy, zr = 0, 0, 0
    k, sigma, min, max, acc, md, p1, p2, r1, r2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if img_name == 'eye3.jpg':
        dx, dy, dr = 248, 232, 221
        zx, zy, zr = 234, 230, 56
        k = 5
        sigma = 33
        min = 62
        max = 68
        acc = 21
        md = 17
        p1 = 50
        p2 = 50
        r1 = 38
        r2 = 255
    elif img_name == 'eye2.bmp':
        zx, zy, zr = 155, 117, 24
        dx, dy, dr = 155, 117, 56
        k = 5
        sigma = 33
        min = 18
        max = 35
        acc = 22
        md = 17
        p1 = 50
        p2 = 50
        r1 = 13
        r2 = 56
    elif img_name == 'eye1.jpg':
        zx, zy, zr = 316, 162, 33
        dx, dy, dr = 319, 163, 106
        k = 7
        sigma = 34
        min = 86
        max = 75
        acc = 22
        md = 8
        p1 = 50
        p2 = 50
        r1 = 19
        r2 = 123

    img = cv.imread(img_name, cv.IMREAD_GRAYSCALE)


    def nothing(*arg):
        pass


    font = cv.FONT_HERSHEY_SIMPLEX
    # org
    org = (50, 50)
    org2 = (50, 150)
    # fontScale
    fontScale = 0.6

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    cv.namedWindow('trackbars')
    # cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", k, 100, nothing)
    cv.createTrackbar("Sigma", "trackbars", sigma, 100, nothing)
    cv.createTrackbar("Min", "trackbars", min, 500, nothing)
    cv.createTrackbar("Max", "trackbars", max, 500, nothing)
    cv.createTrackbar("acc", "trackbars", acc, 30, nothing)
    cv.createTrackbar("Mindist", "trackbars", md, 200, nothing)
    cv.createTrackbar("p1", "trackbars", p1, 200, nothing)
    cv.createTrackbar("p2", "trackbars", p2, 200, nothing)
    cv.createTrackbar("r1", "trackbars", r1, 200, nothing)
    cv.createTrackbar("r2", "trackbars", r2, 300, nothing)

    while (True):
        img = cv.imread(img_name, cv.IMREAD_GRAYSCALE)
        jadro = cv.getTrackbarPos("Jadro", "trackbars") * 2 + 1
        sigma = cv.getTrackbarPos("Sigma", "trackbars") / 10
        min = cv.getTrackbarPos("Min", "trackbars") + 1
        max = cv.getTrackbarPos("Max", "trackbars") + 1
        acc = cv.getTrackbarPos("acc", "trackbars") / 10
        mindist = cv.getTrackbarPos("Mindist", "trackbars")
        p1 = cv.getTrackbarPos("p1", "trackbars")
        p2 = cv.getTrackbarPos("p2", "trackbars")
        r1 = cv.getTrackbarPos("r1", "trackbars") + 1
        r2 = cv.getTrackbarPos("r2", "trackbars") + 1
        blur_img = cv.GaussianBlur(img, (jadro, jadro), sigma)
        edges = cv.Canny(blur_img, min, max)
        cv.imshow("edges", edges)
        circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, acc, mindist, minRadius=r1, maxRadius=r2)
        cimg = cv.imread(img_name)
        # ensure at least some circles were found
        iou = 0
        x1, y1, r1 = 0, 0, 0
        x2, y2, r2 = 0, 0, 0

        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv.circle(cimg, (x, y), r, (0, 255, 0), 2)
                # print('X: %s, Y: %s, r: %s', x, y, r)
                print()
                if r > r1:
                    x1, y1, r1 = x, y, r
                if r < 50:
                    x2, y2, r2 = x, y, r

        union = union_area(x1, y1, r1, dx, dy, dr)
        intersection = intersection_area(x1, y1, r1, dx, dy, dr)
        iou = intersection / (union + 1)
        print(iou)

        text = 'IOU duhovky :' + str(iou)
        image = cv.putText(cimg, text, org, font,
                           fontScale, color, thickness, cv.LINE_AA)

        union = union_area(x2, y2, r2,zx,zy,zr)
        intersection = intersection_area(x2, y2, r2,zx,zy,zr)
        iou = intersection / (union + 1)
        print(iou)

        text = 'IOU zrenicky :' + str(iou)
        image = cv.putText(cimg, text, org2, font,
                           fontScale, color, thickness, cv.LINE_AA)

        cv.imshow("img", cimg)

        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break
