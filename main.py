from operator import le
import numpy as np
from segimages import SegImageGrowing
import os
import cv2


def main():

    os.chdir('./')

    img_inp = cv2.imread('imgs/opencvpy.png',
                         cv2.COLOR_BGR2GRAY)

    img = img_inp[:, :, 0]

    p = SegImageGrowing(img)

    end_img = p.run_segmentation((1, 1), 1, 150)

    cv2.imwrite('./imgs/out.jpg', end_img)


main()

# xmind 1 1 1 130
# tree 55 12 1 115
# buzz/sr 1 1 1 175
# ball 1 1 1 75
# opencv 1, 1, 1, 150
