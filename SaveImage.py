from datetime import datetime
import cv2 as cv

pathtosave = 'C:/Users/Hilt/Pictures/Gradient'
now = datetime.now()

####################################################################
# Save the generated image and return the path to be sent to Twitter
####################################################################
def save_img(randomnum,img):
    imagename= now.strftime("%d_%m_%Y_%H.%M.%S")+ '_randNum_' + str(randomnum)
    filename=pathtosave + '/' + imagename + '.jpg'
    print(filename)
    cv.imwrite(filename, img)
    return filename
