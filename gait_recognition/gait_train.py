import cv2
import numpy as np
import os
import sys
from model.initialization import initialization

# colab version config
conf = {
    "WORK_PATH": "/content/BFHI/gait_recognition/work", # working dir
    "CUDA_VISIBLE_DEVICES": "0,1,2,3",
    "data": {
        'dataset_path': '/content/BFHI/gait_recognition/data/pretreat', # data dir after pretreatment
        'resolution': '64',
        'dataset': 'KTH', # the origin is 'CASIA-B'
        'pid_num': 20, # the number divide train and test
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (8,16), # batch size need to be smaller than pid num
        'restore_iter': 0,
        'total_iter': 500,
        'margin': 0.2,
        'num_workers': 3,
        'frame_num': 30,
        'model_name': 'GaitSet',
    },
}


if __name__ == '__main__':
    m = initialization(conf, train=True)[0]
    print("------------------------------------")

    print("Training START")
    m.fit()
    print("Training COMPLETE")
            