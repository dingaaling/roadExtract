import os

trainPath = os.getcwd() + "/data/train/"
labelPath = os.getcwd() + "/data/label/"

for imName in os.listdir(trainPath):
    if imName.endswith("_sat.jpg"):
        imPath = trainPath  + imName
        imPathNew = labelPath + imName
        os.rename(imPath, imPathNew)
