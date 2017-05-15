from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
np.seterr(over='ignore')
import time
from collections import Counter
from trim import trimImg,pasteInCenter,resizeImg,pasteInCenter50x50,resizeImg50x50
from threshHoldPy import threshold


def createExamples():
    numberArryExamples = open('numArEx.txt','w')
    numbersWeHave = range(0,10)
    versionWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionWeHave:
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarList = str(eiar.tolist())
            numberArryExamples.write(str(eachNum)+'::'+eiarList+'\n')


def creatExamples50x50():
    numberArryExamples = open('numArEx.txt','w')
    numbersWeHave = range(0,10)
    for eachNum in numbersWeHave:
        imgFilePath = 'images/numbers2/'+str(eachNum)+'.png'
        ei = Image.open(imgFilePath)
        eiar = np.array(ei)
        eiarList = str(eiar.tolist())
        numberArryExamples.write(str(eachNum)+'::'+eiarList+'\n')

def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    im = Image.open(filePath)

    im = trimImg(im)

    #8x8 image
    # resizeImg(im)
    # im = pasteInCenter(im)
    # ----------------------

    # 50x50 image
    resizeImg50x50(im)
    im = pasteInCenter50x50(im)
    # ----------------------

    ai = np.array(im)
    threshold(ai)
    im2 = Image.fromarray(ai)
    im2.show()

    iar = np.array(im2)
    iarList = iar.tolist()

    inQuestion = str(iarList)
    eachPixInQ = inQuestion.split('],')
    for eachExample in loadExamps:
        if(len(eachExample)>3):
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')

            x = 0
            while(x<len(eachPixEx)):
                if(eachPixEx[x]==eachPixInQ[x]):
                    matchedAr.append(int(currentNum))
                x+=1
    x = Counter(matchedAr)
    print x

if __name__ == '__main__':
    #createExamples()
    creatExamples50x50()
    whatNumIsThis('test2.png')


