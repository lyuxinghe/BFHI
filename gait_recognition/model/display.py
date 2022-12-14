import os
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import cv2

def display_loss(iter, hard, full, loss_num, dist):
    fig = plt.figure(figsize=(15,5))

    plt.subplot(1,2,1)
    plt.xlabel("iteration index", fontsize=20)
    plt.ylabel("loss metric mean", fontsize=20)
    plt.plot(iter, hard)
    plt.plot(iter, full)
    plt.legend(labels=['hard loss','full loss'], loc=1) # upper right corner
    
    plt.subplot(1,2,2)
    plt.xlabel("iteration index", fontsize=20)
    plt.ylabel("feature mean distance", fontsize=20)
    plt.plot(iter, dist)
    
    dataset = 'KTH'
    img_name = '{}_{}_{}.jpg'.format(dataset, iter[-1], 'loss')
    plt.savefig(img_name)
    plt.show()