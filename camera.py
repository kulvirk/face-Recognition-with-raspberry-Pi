from time import strftime 
import time
from datetime import datetime 
from face_detect import find_face 
import time,os, sys,cv2 
cascadePath ="haarcascade_frontalface_default.xml" 
image_to_detect="face95.jpg"

def take_pic():
    Ntime=datetime.now().strftime('%b,%d,%H:%M:%S')
    camera="sudo fswebcam -S 2 -r 640x480 newface/face95.jpg face95.jpg "
    os.system(camera)
    time.sleep(1)
    photo=cv2.imread(image_to_detect)
    cv2.imshow("you are",photo)
    cv2.waitKey(1000)
       
