import pandas as pd
import cv2 as cv


if __name__ =='__main__':

    df= pd.read_csv('duhovka.csv')
    img=cv.imread('eye3.jpg', cv.IMREAD_GRAYSCALE)

    def nothing(*arg):
        pass
    cv.namedWindow('trackbars')
    cv.imshow("trackbars", img)

    cv.createTrackbar("Jadro", "trackbars", 1, 5, nothing)
    cv.createTrackbar("Sigma", "trackbars", 1, 30, nothing)

    while (True):
        img = cv.imread('eye3.jpg', cv.IMREAD_GRAYSCALE)

        jadro = cv.getTrackbarPos("Jadro", "trackbars")*2+1
        sigma = cv.getTrackbarPos("Sigma", "trackbars")/10

        blur_img = cv.GaussianBlur(img, (jadro, jadro),  sigma)
        cv.imshow("trackbars", blur_img)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break


