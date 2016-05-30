#-*-coding:utf-8-*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    img = cv2.imread('.\degimon.jpg',1)

    """
    ave_color_row = np.average(img, axis=1)
    ave_color = np.average(ave_color_row,axis=0)
    ave_color = np.uint8(ave_color)
    ave_color_img = np.array([[ave_color]*100]*100, np.uint8)
    plt.imshow(ave_color_img)
    plt.show()
    print img
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print gray_img
    """
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    threshold_img = cv2.threshold(gray_img, 60,255,cv2.THRESH_BINARY)
    threshold_img = cv2.cvtColor(threshold_img,cv2.COLOR_GRAY2RGB)
    cv2.imshow('DegimonAdoventure',threshold_img)
    cv2.waitKey(0)


if __name__=='__main__':
    main()
