import numpy as np
import cv2 as cv
import random

xaxis=900
yaxis=800

maxcolor=255

#maximum number of image option
maxoption=1
randomnum=random.randint(0,maxoption)
print(randomnum)

#completely randomized
if(randomnum==0):
    rgb = np.random.randint(255, size=(xaxis,yaxis,3),dtype=np.uint8)
    cv.imshow('RGB',rgb)
    #cv.waitKey(0)

#ramdonizing rectangles on black background
elif(randomnum==1):
    img = np.zeros((xaxis,yaxis,3), np.uint8)
    
    #how many shapes to generate
    randnumofshapes=random.randint(0,255)

    for x in range(randnumofshapes):
        ####adjustable parameters####
        #location variables
        xaxis1=random.randint(0,xaxis)
        xaxis2=random.randint(0,xaxis)
        yaxis1=random.randint(0,yaxis)
        yaxis2=random.randint(0,yaxis)
        #color variables
        color1=random.randint(0,maxcolor)
        color2=random.randint(0,maxcolor)
        color3=random.randint(0,maxcolor)
        #shape thickness
        thickness=random.randint(0,10)
    
        cv.rectangle(img,(xaxis1,xaxis2),(yaxis1,yaxis2),(color1,color2,color3),thickness)
        cv.imshow('shapes',img)
        #cv.waitKey(0)
