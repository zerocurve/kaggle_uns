import sys
import os
import errno
import glob
import cv2
import numpy as np

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

def dice_coefficient(Y_pred, Y):
    """
    This works for one image
    http://stackoverflow.com/a/31275008/116067
    """
    denom = (np.sum(Y_pred == 1) + np.sum(Y == 1))
    if denom == 0:
        # By definition, see https://www.kaggle.com/c/ultrasound-nerve-segmentation/details/evaluation
        return 1
    else:
        return 2 * np.sum(Y[Y_pred == 1]) / float(denom)

def average_dice_coefficient(Y_pred, Y):
    dice_coeffs = []
    for i in range(Y_pred.shape[0]):
        dice_coeffs.append(dice_coefficient(Y_pred[i], Y[i]))
    return np.mean(dice_coeffs)
