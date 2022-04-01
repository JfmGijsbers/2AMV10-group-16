"""
    A Random Forest Classifier that can be saved to preserve the training.

    https://mljar.com/blog/save-load-random-forest/
"""
import joblib
#import numpy as np
from sklearn.model_selection import train_test_split, cross_validate
from data_preprocessing import read_data

from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.utils import plot_model


from random import randint
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Classifier:
    def __init__(self):
        batch_size = 32
        img_height = 180
        img_width = 180

    def predict(self, image):
        """
            Takes an image, converts it to a np array, and uses the model to predict a label.

            Returns:
                pred    String      predicted label
        """
        if not self.rf:
            print("Please fit the model first.")
            return
        test = cv2.imread(image, mode="RGB")
        return self.rf.predict(test)

    def load_data(self):
        """
            Splits the data into a train and a test set.
        """
        self.X, self.y, self.labels = read_data()
        #enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
        #self.X = enc.fit_transform(self.X, self.y)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X_train, self.y_train, test_size=0.25)
        print(f"Shape of training image: {self.X_train[0].shape}")

    def show_images(self, grayscale=False, display_test=False):
        """
            Shows 10 random images from the dataset
        """
        def plot_images(X, y, grayscale=False, display_test=False):
            fig, axes = plt.subplots(1, len(X), figsize=(15,30))
            for n in range(len(X)):
                if grayscale:
                    axes[n].imshow(X[n], cmap='gray')
                else:
                    axes[n].imshow(X[n])
                print(y[n])
                print(np.argmax(y[n]))
                print(self.labels[:5])
                print(self.labels[np.argmin(y[n])])
                axes[n].set_xlabel(self.labels[np.argmin(y[n])])
                axes[n].set_xticks(()), axes[n].set_yticks(())
            plt.show()

        images = [randint(0,len(self.X_train)-1) for i in range(5)]
        X_random = [self.X_train[i] for i in images]
        y_random = [self.y_train[i] for i in images]
        plot_images(X_random, y_random)

        if display_test:
            images = [randint(0,len(self.X_test)) for i in range(5)]
            X_random = [self.X_test[i] for i in images]
            y_random = [self.y_test[i] for i in images]
            plot_images(X_random, y_random)


    def build(self):
        """
            Fits the model
        """
        model = models.Sequential()
        model.add(layers.Conv2D(512, (3, 3), activation='relu',
                                input_shape=IMG_SHAPE))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(256, (3, 3), activation='relu',
                                input_shape=IMG_SHAPE))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.3))
        model.add(layers.Flatten())
        #model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dense(len(self.labels), activation='sigmoid'))
        rmsprop_optimizer = keras.optimizers.RMSprop(learning_rate=0.001)

        model.compile(
            optimizer=rmsprop_optimizer,
            loss="categorical_crossentropy",
            metrics=['accuracy']
        )
        self.model = model

    def evaluate(self, train=None, stop_training=False, generator=None):
        learning_curves = {}
        if train and not stop_training:
            if generator:
                # TODO: deploy generator
                pass
            else:
                history = self.model.fit(
                    self.X_train, self.y_train, epochs=3, batch_size=3,
                    verbose=1, validation_data=(self.X_val, self.y_val))
                learning_curves = history.history
            # TODO: save to file
        else:
            # TODO: load from file
            pass
        lc = pd.DataFrame(learning_curves)
        print(f"Max val score: {lc.iloc[:,3].max()*100}%")
        lc.plot(lw=2, style=['b:', 'r:', 'b-', 'r-'])
        plt.xlabel('epochs')
        plt.show()

        print(self.model.summary())
        plot_model(self.model)

                

    def test(self):
        """
            Get accuracy scores based X_test and y_test
            TODO implement
        """
        if not self.X_test:
            self.train()
        xvals = cross_validate(self.rf, self.X, self.y, return_train_score=True, n_jobs=-1)
        return xvals['train_score'], xvals['test_score']

    def feature_importance(self, nr_images=10, nr_rows=2):
        """
            Plot graphs with images and importances
            for nr_images images on nr_rows rows

            TODO implement
        """
        fig, ax = plt.subplots(nr_images, nr_rows)
        pass

    def misclassifications(self):
        """
            Plot items with their misinterpreted label
        """
        y_pred = self.rf.predict(self.X_test)
        misclassified = np.nonzero(y_pred != list(self.y_test))[0]

    def save(self):
        if not self.rf:
            print("Unable to save model since it doesn't exist")
        joblib.dump(self.rf, "./random_forest.joblib", compress=3)

    def load(self):
        self.rf = joblib.load("./random_forest.joblib")
