import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image

def load_image(fileName):
    return mpimg.imread(fileName)

def display_image(fileName):
    imgPlot = plt.imshow(fileName)
    plt.show()

def feature_extract(imgPatch):

    mean = np.mean(imgPatch, axis=(0,1))
    std = np.std(imgPatch, axis=(0,1))
    features = np.append(mean, std)
    return features

def img_crop(img, w, h, stride, padding):

    cropList = []

    imgWidth, imgHeight =img.shape[0], img.shape[1]
    img = np.lib.pad(img, ((padding, padding), (padding, padding), (0,0)), "reflect")

    for i in range(padding,imgHeight+padding,stride):
        for j in range(padding,imgWidth+padding,stride):
            im_patch = img[j-padding:j+w+padding, i-padding:i+h+padding, :]
            cropList.append(im_patch)
    return cropList


if __name__ == "__main__":

    trainPath = os.getcwd() + "/data/sample/"
    maskPath = os.getcwd() + "/data/mask/"

    for imName in os.listdir(trainPath):
        imPath = trainPath + imName
        img = load_image(imPath)
        crops = img_crop(img, 3, 3, 1, 0)
    print(len(crops))
    print(crops[0].shape)
