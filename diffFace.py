import face_recognition
from glob import iglob
import os
from pathlib import Path
import csv
import shutil
from PIL import Image
import cv2
from skimage.measure import compare_ssim
import imutils
import numpy as np
#from facecrop import FaceCrop

class DiffFace:

    def traverseDir(self):
        rootdir_glob = '/home/android/Downloads/Race/**/**/*' # Note the added asterisks
        # This will return absolute paths
        file_list = [f for f in iglob('**/*.jpg', recursive=True) if os.path.isfile(f)]
        return file_list

    def track(self,filename):
        if not os.path.isfile(str(Path().absolute())+'/'+filename):
            with open(filename,'w') as a:
                pass
        if os.stat(filename).st_size==0:
            with open(filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
                    writer.writeheader()

    def facediff(self,imageA,imageB):
                try:
                    
                    #Checking the dimention
                    height, width, depth=imageA.shape

                    image1=imageA.shape
                    imageB=cv2.resize(imageB,(width,height))
                    image2=imageB.shape


                    #print(imageA.shape ,image2)
                    
                    if not image1==image2:
                        print("images are diff dimentions.....")
                    else:
                        #print("the images are same dimentions.....")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = compare_ssim(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("SSIM: {}".format(score))
                        
                    if score > 0.5 :
                        print("Duplicate image found")
                    return score   
                except Exception as e:
                    print(e)
                

if __name__ == "__main__":
    fieldnames=['oldpath','newpath']
    filename='diffhistorydlib.csv'
    diffFace=DiffFace()
    diffFace.facediff()