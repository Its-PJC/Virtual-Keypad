import cv2
import numpy as np
import handTrackMod as htm
from math import *
import imutils
import os
import time


def showImg(img, image, x1, y1, x2, y2, image_ratio, hCam, wCam):
    y, x = (x1 + x2) // 2, (y1 + y2) // 2
    length = hypot(x2 - x1, y2 - y1) + 1
    ang = atan2((y2 - y1), (x2 - x1)) * 180 / 3.14

    wImage = int(length)
    hImage = int(wImage * image_ratio)

    re_image = cv2.resize(image, (wImage, hImage), interpolation=cv2.INTER_AREA)
    ro_image = imutils.rotate(re_image, 360 - ang)

    for i in range(hImage):
        for j in range(wImage):
            if 0 <= x - hImage // 2 + i < hCam and 0 <= y - wImage // 2 + j < wCam:
                if ro_image[i][j][0] != 0 and ro_image[i][j][1] != 0 and ro_image[i][j][2] != 0:
                    img[x - hImage // 2 + i][y - wImage // 2 + j] = ro_image[i][j]
    return img


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)

src = "C:/Users/Pranav J Chiddarwar/PycharmProjects/VirtualKeypad/Numbers/"

# Reading all 12 images
img0 = cv2.imread(src + "0.png")
img1 = cv2.imread(src + "1.png")
img2 = cv2.imread(src + "2.png")
img3 = cv2.imread(src + "3.png")
img4 = cv2.imread(src + "4.png")
img5 = cv2.imread(src + "5.png")
img6 = cv2.imread(src + "6.png")
img7 = cv2.imread(src + "7.png")
img8 = cv2.imread(src + "8.png")
img9 = cv2.imread(src + "9.png")
imgStar = cv2.imread(src + "star.png")
imgHash = cv2.imread(src + "hash.png")

image_ratio = img1.shape[0] / img1.shape[1]
arr = [0]*12

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        fingers = detector.fingersUp()
        # print(fingers)
        # Show 1
        img = showImg(img, img1, lmList[8][1], lmList[8][2],
                      lmList[7][1], lmList[7][2], image_ratio, hCam, wCam)
        # if lmList[7][2]<lmList[4][2]<lmList[8][2]:
        if detector.findDistance(4,8,img,draw=False)<20:
            arr[1]=1
            print(arr)

        # Show 2
        img = showImg(img, img2, lmList[7][1], lmList[7][2],
                      lmList[6][1], lmList[6][2], image_ratio, hCam, wCam)
        if lmList[6][2]<lmList[4][2]<lmList[7][2]:
            arr[2]=1
            print(arr)

        # Show 3
        img = showImg(img, img3, lmList[6][1], lmList[6][2],
                      lmList[5][1], lmList[5][2], image_ratio, hCam, wCam)
        if lmList[5][2]<lmList[4][2]<lmList[6][2]:
            arr[3]=1
            print(arr)

        # Show 4
        img = showImg(img, img4, lmList[12][1], lmList[12][2],
                      lmList[11][1], lmList[11][2], image_ratio, hCam, wCam)

        # Show 5
        img = showImg(img, img5, lmList[11][1], lmList[11][2],
                      lmList[10][1], lmList[10][2], image_ratio, hCam, wCam)

        # Show 6
        img = showImg(img, img6, lmList[10][1], lmList[10][2],
                      lmList[9][1], lmList[9][2], image_ratio, hCam, wCam)

        # Show 7
        img = showImg(img, img7, lmList[16][1], lmList[16][2],
                      lmList[15][1], lmList[15][2], image_ratio, hCam, wCam)

        # Show 8
        img = showImg(img, img8, lmList[15][1], lmList[15][2],
                      lmList[14][1], lmList[14][2], image_ratio, hCam, wCam)

        # Show 9
        img = showImg(img, img9, lmList[14][1], lmList[14][2],
                      lmList[13][1], lmList[13][2], image_ratio, hCam, wCam)

        # Show star
        img = showImg(img, imgStar, lmList[20][1], lmList[20][2],
                      lmList[19][1], lmList[19][2], image_ratio, hCam, wCam)

        # Show 0
        img = showImg(img, img0, lmList[19][1], lmList[19][2],
                      lmList[18][1], lmList[18][2], image_ratio, hCam, wCam)

        # Show hash
        img = showImg(img, imgHash, lmList[18][1], lmList[18][2],
                      lmList[17][1], lmList[17][2], image_ratio, hCam, wCam)

        arr = [0]*12

    cv2.imshow("Keypad", img)
    cv2.waitKey(1)
