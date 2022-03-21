"""
    Returns a cleaned X and y dataset to be used for classification.
"""
import os
import cv2

def read_data():
    """
        Reads the images and returns them as arrays X and y

        returns: X      array containing np-array-representation of images
                 y      array containing corresponding labels
    """
    os.chdir('./data/trainingData/TrainingImages')
    X = []
    y = []
    for label in [name for name in os.listdir(".") if os.path.isdir(name)]:
        for image in [name for name in os.listdir(f"./{label}")]:
            X.append(cv2.imread(image, mode="RGB"))
            y.append(label)
    return X, y

read_data()