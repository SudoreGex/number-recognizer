from PIL import Image, ImageChops
from threshHoldPy import threshold
import numpy as np
import matplotlib.pyplot as plt

def trimImg(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

#for 8x8 Image
def pasteInCenter(im):
    newImg = Image.new(im.mode, (8, 8), "white")
    w1, h1 = (8, 8)
    # trimmedImage = trimImg(im)
    # w2, h2 = trimmedImage.size
    w2,h2 = im.size
    newImg.paste(im,((w1-w2)/2,(h1-h2)/2))
    return newImg

def resizeImg(im):
    w=8
    h=8
    w1,h1 = im.size
    if(h<h1 and w>=w1):
        im.thumbnail((w1,h), Image.ANTIALIAS)
    elif(h>=h1 and w<w1):
        im.thumbnail((w,h1), Image.ANTIALIAS)
    elif(h<h1 and w<w1):
        im.thumbnail((w,h), Image.ANTIALIAS)

#for 50x50 Image
def pasteInCenter50x50(im):
    newImg = Image.new(im.mode, (50, 50), "white")
    w1, h1 = (50, 50)
    # trimmedImage = trimImg(im)
    # w2, h2 = trimmedImage.size
    w2,h2 = im.size
    newImg.paste(im,((w1-w2)/2,(h1-h2)/2))
    return newImg

def resizeImg50x50(im):
    w=50
    h=50
    w1,h1 = im.size
    if(h<h1 and w>=w1):
        im.thumbnail((w1,h), Image.ANTIALIAS)
    elif(h>=h1 and w<w1):
        im.thumbnail((w,h1), Image.ANTIALIAS)
    elif(h<h1 and w<w1):
        im.thumbnail((w,h), Image.ANTIALIAS)

if __name__ == '__main__':
    im = Image.open("test2.png")


    im = trimImg(im)
    #resizeImg(im)
    im = pasteInCenter50x50(im)
    #ai = np.array(im)
    #threshold(ai)
    #im2 = Image.fromarray(ai)
    im.show()