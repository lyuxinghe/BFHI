from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import cv2

def display_loss(iter, hard, full, loss_num, dist):
    fig = plt.figure()
    plt.subplot(1,2,1)
    plt.xlabel("iteration index") 
    plt.ylabel("loss metric")
    # plt.title("per-frame residual") 
    plt.plot(iter, hard)
    plt.plot(iter, full) 
    # plt.savefig("residual plot.png")
    
    plt.subplot(1,2,2)
    plt.xlabel("iteration index") 
    plt.ylabel("feature mean dist")
    # plt.title("per-frame mean distances") 
    plt.plot(iter, dist) 
    # plt.savefig("mean distances plot.png")
    plt.show()