import numpy as np
import cv2 as cv
import random
from SaveImage import save_img
from Twitter import tweet_image

xaxis=900
yaxis=800

maxcolor=255

#maximum number of image option
maxoption=1
randomnum=4#random.randint(0,maxoption)
print(randomnum)

#completely randomized
if(randomnum==0):
    rgb = np.random.randint(255, size=(xaxis,yaxis,3),dtype=np.uint8)
    cv.imshow('RGB',rgb)
    #cv.waitKey(0)

#randomizing rectangles on black background
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
    filename=save_img(randomnum,img)

#pixalate image
elif(randomnum==2):
    print("Not yet implented - image pixalization")

#drawing over image
elif(randomnum==3):
    print("Not yet implemented - image sketching")

#repeating pattern
elif(randomnum==4):
    img = np.zeros((xaxis,yaxis,3), np.uint8)
    
    ####adjustable parameters####
    #location variables
    xaxis1=0
    xaxis2=100
    yaxis1=0
    yaxis2=100
    #color variables
    color1=random.randint(0,maxcolor)
    color2=random.randint(0,maxcolor)
    color3=random.randint(0,maxcolor)
    #shape thickness
    thickness=random.randint(0,10)
    #space between shape
    shapespacing = 1

    for x in range(50):
        cv.rectangle(img,(xaxis1,xaxis2),(yaxis1,yaxis2),(color1,color2,color3),thickness)
        xaxis1=xaxis1+100 #shift over to last x-axis endpoint
        xaxis2=xaxis2+100
    cv.imshow('repeat',img)
    filename=save_img(randomnum,img)

tweet_image(filename)
#insta_image(filename)

#code to use eventually to vary up shape creation
"""
        randnum = np.random.randint(0,3)
        if(randnum==1):
            cv.circle
        elif(randnum==2):
            cv.ellipse
        elif(randnum==3):
"""
