"""
    Make the actual prediction. This file uses a saved version of the trained model in order to prevent
    having to re-train the model each time.
"""
import joblib
import errno
import os

MODEL_LOC = "./random_forest.joblib"

loaded_rf = joblib.load(MODEL_LOC)

raise FileNotFoundError(
    errno.ENOENT, os.strerror(errno.ENOENT), MODEL_LOC)
    
