from ntpath import join
from random import random
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
import cv2
import numpy as np
import math
import ctypes
import os

from pyparsing import col




class ShowMatrixPic():
    def __init__(self, row=0, column=0, atuoTile=False, width=200, height=200, text='None'):
        super(ShowMatrixPic, self).__init__()
        self.row = row
        self.column = column
        self.atuoTile = atuoTile
        self.width = width
        self.height = height
        self.text = text
        if self.row < 0:
            self.row = 0
        if self.column < 0:
            self.column = 0


        # user32 = ctypes.windll.user32
        # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # print(screensize)
        #

    def __rawAndColumn(self,imgList):
        r = c = 0
        resSubtraction = 1
        if self.column == 0 and self.row == 0:
            lenList = len(imgList)
            k = round(math.sqrt(lenList))
            if k > 5:
                r = 5
                if lenList % r == 0:
                    c = lenList // k
                else:
                    num2 = lenList // r
                    if num2 > r:
                        c = k + (num2 - r)
                    else:
                        c = k + num2


            else:
                r = k
                if lenList % r == 0:
                    c = lenList // r
                else:
                    u = r ** 2
                    num2 = lenList % r
                    if u < lenList:
                        if num2 < r:
                            c = r + 1
                        else:
                            c = r + num2
                    else:
                        c = r
        elif self.column == 0 and self.row != 0:
            lenList = len(imgList)
            r = self.row
            c = math.ceil(lenList / self.row)
        elif self.column != 0 and self.row == 0:
            lenList = len(imgList)
            c = self.column
            r = math.ceil(lenList / self.column)
        else:
            r = self.row
            c = self.column

        return r, c

    def showVideo(self, imgList):

        r, c = self.__rawAndColumn(imgList)


        image = []
        l = len(imgList)
        print(l)
        for img in imgList:
            # print(img)
            if img is not None:
                img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            else:
                img = np.zeros((self.height, self.width, 3), np.uint8)
                textSize = round(self.width * 0.005, 2)
                textThickness = round(self.width / 100)
                cv2.putText(img, self.text, ((self.width // 4), (self.height // 2)), cv2.FONT_HERSHEY_COMPLEX,
                            textSize, (255, 255, 255), textThickness)

            image.append(img)




        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThickness = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThickness)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)
        else:
            lenOfimg = len(imgList)
            tableNum = r * c

            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    if o > lenOfimg:
                        image.append(image[o % lenOfimg])
                    else:
                        image.append(image[o])


        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal

    def showPic(self, imgList):

        r, c = self.__rawAndColumn(imgList)

        image = []
        l = len(imgList)
        print(l)
        for i in range(l):
            
            #img = cv2.imread(imgList[i])
            
            #HERE YOU CAN CHANGE DISPLAY IMAGE TO GREYSCALE
            # turn image to greyScale
            #img = cv2.imread(imgList[i], cv2.IMREAD_GRAYSCALE)

            img = cv2.imread(imgList[i])

            img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            image.append(img)
        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThick = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThick)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)

        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal, img

def main():
    
    subdivideImageActualTransformation('girl.jpg', "photos", "results", 20, makeDirectoryOfInputPictures("photos"))
    

 
    
def makeDirectoryOfInputPictures(fromDirectory):
    #https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
    import os, os.path

    
    array1 = []
    array2 = []
    array3 = []
    array4 = []
    array5 = []
    array6 = []
    array7 = []
    array8 = []
    array9 = []
    array10 = []
    array11 = []
    array12 = []
    array13 = []
    array14 = []
    array15 = []
    array16 = []
    array17 = []
    array18 = []
    array19 = []
    array20 = ['photos/white.jpg']



    imgFolders = [array1, array2, array3, array4, array5, array6, array7, array8, array9, array10, 
                    array11,array12,array13,array14,array15,array16,array17,array18,array19, array20]

    imgFolders = sortInputPicturesIntoDirecoty(fromDirectory,imgFolders)

    '''
    path_of_directory = fromDirectory
    ext = ('jpg')
    


    for files in os.listdir(path_of_directory):
                if files.endswith(ext):
                    greyVal = analyseImageReturnValueBetweenZeroAndOne(os.path.join(path_of_directory,files))
                    if(greyVal <=  0.05):
                        array1.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.05 and greyVal <= 0.1):
                        array2.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.1 and greyVal <= 0.15):
                        array3.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.15 and greyVal <= 0.2):
                        array4.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.2 and greyVal <= 0.25):
                        array5.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.25 and greyVal <= 0.3):
                        array6.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.3 and greyVal <= 0.35):
                        array7.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.35 and greyVal <= 0.4):
                        array8.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.4 and greyVal <= 0.45):
                        array9.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.45 and greyVal <= 0.5):
                        array10.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.5 and greyVal <= 0.55):
                        array11.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.55 and greyVal <= 0.6):
                        array12.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.6 and greyVal <= 0.65):
                        array13.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.65 and greyVal <= 0.7):
                        array14.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.7 and greyVal <= 0.75):
                        array15.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.75 and greyVal <= 0.8):
                        array16.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.8 and greyVal <= 0.85):
                        array17.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.85 and greyVal <= 0.9):
                        array18.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.9 and greyVal <= 0.95):
                        array19.append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.95 and greyVal <= 0.1):
                        array20.append(os.path.join(path_of_directory,files))
                        continue
    ''' 
        
    print(imgFolders)    
    print("array1")
    print(array6)  
    return imgFolders
         
def sortInputPicturesIntoDirecoty(fromDirectory,imgFolders):
    path_of_directory = fromDirectory
    ext = ('jpg')

    for files in os.listdir(path_of_directory):
                if files.endswith(ext):
                    greyVal = analyseImageReturnValueBetweenZeroAndOne(os.path.join(path_of_directory,files))
                    if(greyVal <=  0.05):
                        imgFolders[0].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.05 and greyVal <= 0.1):
                        imgFolders[1].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.1 and greyVal <= 0.15):
                        imgFolders[2].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.15 and greyVal <= 0.2):
                        imgFolders[3].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.2 and greyVal <= 0.25):
                        imgFolders[4].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.25 and greyVal <= 0.3):
                        imgFolders[5].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.3 and greyVal <= 0.35):
                        imgFolders[6].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.35 and greyVal <= 0.4):
                        imgFolders[7].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.4 and greyVal <= 0.45):
                        imgFolders[8].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.45 and greyVal <= 0.5):
                        imgFolders[9].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.5 and greyVal <= 0.55):
                        imgFolders[10].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.55 and greyVal <= 0.6):
                        imgFolders[11].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.6 and greyVal <= 0.65):
                        imgFolders[12].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.65 and greyVal <= 0.7):
                        imgFolders[13].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.7 and greyVal <= 0.75):
                        imgFolders[14].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.75 and greyVal <= 0.8):
                        imgFolders[15].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.8 and greyVal <= 0.85):
                        imgFolders[16].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.85 and greyVal <= 0.9):
                        imgFolders[17].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.9 and greyVal <= 0.95):
                        imgFolders[18].append(os.path.join(path_of_directory,files))
                        continue
                    if(greyVal > 0.95 and greyVal <= 0.1):
                        imgFolders[19].append(os.path.join(path_of_directory,files))
                        continue

    return imgFolders                
         

def analyseImageReturnValueBetweenZeroAndOne(pathToPicture):

    # this is my source for this function
    # https://stackoverflow.com/questions/35586206/how-to-get-an-average-pixel-value-of-a-gray-scale-image-in-python-using-pil-nump
    from skimage import io, img_as_float
    import numpy as np

    image = io.imread(pathToPicture)
    image = img_as_float(image)
    print(np.mean(image))
    return np.mean(image)


def subdivideImageActualTransformation(filename, dir_in, dir_out, d, pictureArray):
    # this is my source for this function
    # https://stackoverflow.com/questions/5953373/how-to-split-image-into-multiple-pieces-in-python
    import os
    from PIL import Image
    from itertools import product
    import uuid

    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))


    #### MAIN Methode COPY
    smp = ShowMatrixPic(width=1000, height=1000, row=50, column=50, atuoTile=False)
 
    imgListOne = []

    import random

    for j in range(0, 1000,d):
        for i in range(0,1000,d):
            box = (j, i, j+d, i+d)
            out = os.path.join(dir_out, f'{name}{i}{j}{ext}')
                    
            img.crop(box).save(out)
            colorVal = analyseImageReturnValueBetweenZeroAndOne(out)
            #this will remove each generated image from the results directory
            os.remove(out)
            
            result = appendImageToFinalArray(pictureArray,imgListOne,colorVal)
            pictureArray = result[0]
            imgListOne = result[1]


    printInfo(pictureArray)

    resultPic = smp.showPic(imgListOne)
    numpy_horizontal = resultPic[0]

    # try to save image to photos directory
    picName = str(uuid.uuid4())+'.jpg'

    #show pic directly 
    #cv2.imshow('CroppedImage', numpy_horizontal)
 

    cv2.imwrite(picName, numpy_horizontal, [cv2.IMWRITE_JPEG_QUALITY, 10])

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def printInfo(picArray):
    
    print("  .....  ")

    '''
        for i in len(picArray):
        print('The Array: ')
        if(len(picArray[i])):
            print('ArrayEmpty')
        else:
            for count in len(picArray[i]):
                print(picArray[i][count])
            print(len(picArray[i]))

    '''

def appendImageToFinalArray(pictureArray, imgListOne, colorVal):
    import random

    if(colorVal <=  0.05):
        imgListOne.append(random.choice(pictureArray[0]))    

    if(colorVal >  0.05 and colorVal <= 0.1):
        imgListOne.append(random.choice(pictureArray[1]))    

    if(colorVal >  0.1 and colorVal <= 0.15):
        imgListOne.append(random.choice(pictureArray[2]))    

    if(colorVal >  0.15 and colorVal <= 0.2):
        imgListOne.append(random.choice(pictureArray[3]))    

    if(colorVal >  0.2 and colorVal <= 0.25):
        imgListOne.append(random.choice(pictureArray[4]))    

    if(colorVal >  0.25 and colorVal <= 0.3):
        imgListOne.append(random.choice(pictureArray[5]))    

    if(colorVal >  0.3 and colorVal <= 0.35):
        imgListOne.append(random.choice(pictureArray[6]))    

    if(colorVal >  0.35 and colorVal <= 0.4):
        imgListOne.append(random.choice(pictureArray[7]))    
    
    if(colorVal >  0.4 and colorVal <= 0.45):
        imgListOne.append(random.choice(pictureArray[8]))    

    if(colorVal >  0.45 and colorVal <= 0.5):
        imgListOne.append(random.choice(pictureArray[9]))    

    if(colorVal >  0.5 and colorVal <= 0.55):
        imgListOne.append(random.choice(pictureArray[10]))    

    if(colorVal >  0.55 and colorVal <= 0.6):
        imgListOne.append(random.choice(pictureArray[11]))    

    if(colorVal >  0.6 and colorVal <= 0.65):
        imgListOne.append(random.choice(pictureArray[12]))    

    if(colorVal >  0.65 and colorVal <= 0.7):
        imgListOne.append(random.choice(pictureArray[13]))    

    if(colorVal >  0.7 and colorVal <= 0.75):
        imgListOne.append(random.choice(pictureArray[14]))    

    if(colorVal >  0.75 and colorVal <= 0.8):
        imgListOne.append(random.choice(pictureArray[15]))    

    if(colorVal >  0.8 and colorVal <= 0.85):
        imgListOne.append(random.choice(pictureArray[16]))    

    if(colorVal >  0.85 and colorVal <= 0.9):
        imgListOne.append(random.choice(pictureArray[17]))    

    if(colorVal > 0.9 and colorVal <= 0.95):
        imgListOne.append(random.choice(pictureArray[18]))    

    if(colorVal > 0.95 and colorVal <= 1):
        imgListOne.append(random.choice(pictureArray[19])) 
    
    if(colorVal > 1):
        #print default inside final picture     
        imgListOne.append('photos/white.jpg')
        
    return pictureArray, imgListOne    


if __name__ == "__main__":
    main()

main()








