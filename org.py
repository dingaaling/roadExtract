import os

trainPath = os.getcwd() + "/data/train/"
maskPath = os.getcwd() + "/data/mask/"

for imName in os.listdir(trainPath):
    if imName.endswith("_mask.png"):
        imPath = trainPath  + imName
        imPathNew = maskPath + imName
        os.rename(imPath, imPathNew)
