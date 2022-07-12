from typing import List, Tuple
import numpy as np
from segimages import SegImageGrowing
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():

    os.chdir('./')

    img_inp = cv2.imread('imgs/opencvpy.png',
                         cv2.COLOR_BGR2GRAY)

    img = img_inp[:, :, 0]

    seg_growing = SegImageGrowing(img)

    img_seg, events_seg = seg_growing.run_segmentation((1, 1), 1, 150)

    start_animation(img_seg.shape, events_seg)

    #cv2.imwrite('./imgs/out.jpg', img_seg)


def start_animation(shape, event_arr:List[Tuple[int, int, int]]):

    mt_ani = np.zeros(shape)

    fig = plt.figure()

    l = plt.plot(mt_ani)

    def updatefig(k):
        print(k)

    ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
    plt.show()


main()

# xmind 1 1 1 130
# tree 55 12 1 115
# buzz/sr 1 1 1 175
# ball 1 1 1 75
# opencv 1, 1, 1, 150
