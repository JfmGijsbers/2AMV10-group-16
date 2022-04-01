"""
    Returns a cleaned X and y dataset to be used for classification.
"""
import os
import cv2
import sys
import numpy as np
from PIL import Image
import tensorflow as tf
from scipy import misc
from matplotlib.image import imread

PATH=r"C:\Users\Jeroen Gijsbers\OneDrive - TU Eindhoven\Uni\Master\Jaar 1\Kwartiel 3\2AMV10 - Visual Analytics\Project\2AMV10-group-16"
IMG_SIZE = 180

def read_data():
    """
        Reads the images and returns them as arrays X and y

        returns: X      array containing np-array-representation of images
                 y      array containing corresponding labels
    """
    #print(os.curdir)
    #os.chdir('../data/trainingData/TrainingImages')
    X = []
    y = []
    labels = []
    sys.path.insert(0, PATH)
    path = "./data/trainingData/TrainingImages"
    i = 0
    limit = 200
    for label in [name for name in os.listdir(path) if os.path.isdir(f"{path}/{name}")]:
        labels.append(label)
        for image in [name for name in os.listdir(f"{path}/{label}")]:
            #X.append(cv2.imread(f"{path}/{label}/{image}"))
            try:
                img = cv2.imread(f"{path}/{label}/{image}")
                X.append(img)
                y.append(label)
                i+= 1
            except:
                print("something went wrong, probably .db file")
            if i == limit:
                break
        if i == limit:
            break
    return np.array(X), y, labels#.reshape(50, 256*256), y, labels