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



if __name__ == "__main__":

    trainPath = os.getcwd() + "/data/train/"
    maskPath = os.getcwd() + "/data/mask/"

    for imName in os.listdir(trainPath):
        imPath = trainPath + imName
        im = load_image(imPath)
