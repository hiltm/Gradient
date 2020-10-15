import numpy as np
import cv2 as cv
import random

xaxis=900
yaxis=800

#maximum number of image option
maxoption=1
randomnum=random.randint(0,maxoption)
print(randomnum)

#completely randomized
if(randomnum==0):
    rgb = np.random.randint(255, size=(xaxis,yaxis,3),dtype=np.uint8)
    cv.imshow('RGB',rgb)
    #cv.waitKey(0)

#ramdonizing images on black background
elif(randomnum==1):
    img = np.zeros((xaxis,yaxis,3), np.uint8)
    cv.rectangle(img,(384,0),(510,128),(0,255,0),10)
    cv.imshow('shapes',img)
    #cv.waitKey(0)
