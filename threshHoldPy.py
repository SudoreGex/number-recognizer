from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
np.seterr(over='ignore')
import time

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x ,y:x+y,eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x ,y: x+y, balanceAr)/len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x,y:x+y,eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr
