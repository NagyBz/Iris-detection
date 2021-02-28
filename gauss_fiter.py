import pandas as pd
import cv2 as cv


if __name__ =='__main__':

    df= pd.read_csv('duhovka.csv')
    img=cv.imread('eye3.bmp',cv.IMREAD_GRAYSCALE)

    def nothing(*arg):
        pass
    cv.namedWindow('trackbars')
    cv.imshow("trackbars", img)
    cv.createTrackbar("Jadro", "trackbars", 0, 50, nothing)
    cv.createTrackbar("Sigma", "trackbars", 0, 10, nothing)

    while (True):
        jadro = cv.getTrackbarPos("Jadro", "trackbars");
        sigma = cv.getTrackbarPos("Sigma", "trackbars");
        blur_img = cv.GaussianBlur(img, (5, 5), jadro, sigma)
        cv.imshow("trackbars", blur_img)
        k = cv.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv.destroyAllWindows()
            break


