import cv2
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from PIL import Image

OUTPUT_PATH = './data/output/' # set the real output path
INPUT_PATH = './data/walking/'

def display_video(path):
    cap = cv2.VideoCapture(path)
    f_list = list()

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            f_list.append(frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break
    
    cap.release()
    cv2.destroyAllWindows()

    return f_list


def image_enhancement(frame):
    err_kernel = np.ones((3, 3), np.uint8)
    dil_kernel = np.ones((3, 3), np.uint8)

    img_erosion = cv2.erode(frame, err_kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion, dil_kernel, iterations=1)
    return img_dilation

def set_new_repo(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("new folder: %s" %path)
    else:
        print("update folder: %s" %path)

'''
source: https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html
'''
def background_subtract(path, sub_name):
    full_path = os.path.join(OUTPUT_PATH, sub_name)
    set_new_repo(full_path)

    backSub = cv2.createBackgroundSubtractorKNN()
    backSub. setHistory(600)
    backSub.setShadowThreshold(0.6)
    backSub.setDist2Threshold(1200)
    capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(path))
    if not capture.isOpened():
        print('Unable to open: ' + path)
        exit(0)

    while True:
        ret, frame = capture.read()
        idx = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
        if frame is None:
            break
        
        fgMask1 = backSub.apply(frame) # background subtraction
        _, fgMask2 = cv2.threshold(fgMask1, 200, 255, type=0) # get rid of shadow
        fgMask3 = cv2.medianBlur(fgMask2, 3) # median filter
        fgMask = image_enhancement(fgMask3) # image morphology

        if np.count_nonzero(fgMask) > 800:
            frame_name = "silho_%d.jpg" %idx
            save_path = os.path.join(full_path, frame_name)
            cv2.imwrite(save_path, fgMask)
            # plot the result
            # fig = plt.figure(figsize=(14, 4))
            # ax1 = fig.add_subplot(1,3,1)  
            # ax1.imshow(frame)
            # ax1.set_title("frame: %d"%idx)
            # ax2 = fig.add_subplot(1,3,2)  
            # ax2.imshow(fgMask1, cmap='gray')
            # ax2.set_title("background substraction")
            # ax3 = fig.add_subplot(1,3,3)
            # ax3.imshow(fgMask, cmap='gray')
            # ax3.set_title("silhouette")
            # plt.savefig("%s/result_%d.jpg" %(full_path, idx))
            # plt.show()
            
        else:
            print("Working on frame %d, no silhouette" %idx)
        
# main
os.chdir('./cv_project/')
id_list = os.listdir(INPUT_PATH)
id_list.sort()
# Walk the input path
for _id in id_list:
    path = os.path.join(INPUT_PATH, _id)
    background_subtract(path, _id)