"""
    A Random Forest Classifier that can be saved to preserve the training.

    https://mljar.com/blog/save-load-random-forest/
"""
import joblib
#import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import cv2
import matplotlib as plt

class Classifier:
    def __init__(self):
        pass

    def predict(self, image):
        """
            Takes an image, converts it to a np array, and uses the model to predict a label.

            Returns:
                pred    String      predicted label
        """
        if not self.rf:
            print("Please fit the model first.")
            return
        cv2.imread(image, mode="RGB")

    def load_data(self):
        """
            Splits the data into a train and a test set.
        """
        pass

    def train(self):
        """
            Fits the model
        """
        if not self.X_train:
            self.load_data()
        self.rf = RandomForestClassifier()
        rf.fit(self.X_train, self.y_train)

    def test(self):
        """
            Get accuracy scores based X_test and y_test
            TODO implement
        """
        if not self.X_test:
            self.train()
        pass

    def feature_importance(self, nr_images=10, nr_rows=2):
        """
            Plot graphs with images and importances
            for nr_images images on nr_rows rows

            TODO implement
        """
        fig, ax = plt.subplots(nr_images, nr_rows)
        pass

    def save(self):
        if not self.rf:
            print("Unable to save model since it doesn't exist")
        joblib.dump(self.rf, "./random_forest.joblib", compress=3)

    def load(self):
        self.rf = joblib.load("./random_forest.joblib")

iris = load_iris()
X = iris.data
y = iris.target

rf = RandomForestClassifier()
rf.fit(X,y)

joblib.dump(rf, "./random_forest.joblib", compress=3)
#loaded_rf = joblib.load("./random_forest.joblib")