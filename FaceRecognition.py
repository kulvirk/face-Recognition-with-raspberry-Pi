import time
from Adafruit_CharLCD import Adafruit_CharLCD
lcd=Adafruit_CharLCD()
import RPi.GPIO as GPIO
from face_detect import find_face
from images_labels import get_images_and_labels
from names import names_to_num
from camera import  take_pic
from recognizer import recog
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.createLBPHFaceRecognizer()

camera=" sudo fswebcam -r 320x240 newface/subject95.jpg subject95.jpg -S 2"
path='./savedfaces'
path1='./newface'
image_to_detect="subject95.jpg"


find_face(cascadePath,image_to_detect)
images,labels=get_images_and_labels(path,faceCascade)
lcd.clear()
lcd.message("Loading.....")
cv2.destroyAllWindows()
recognizer.train(images,np.array(labels))


while True:
        i=GPIO.input(23)
        if i==1:
                lcd.clear()
                lcd.message("Stop,let me know you")
                time.sleep(2)
                take_pic(camera,image_to_detect)
                lcd.clear()
                lcd.message("finding....you")
                nbr_predicted,conf=recog(path1,faceCascade,recognizer)
                try :
                    nbr_predicted=int(nbr_predicted)
                    yes=names_to_num(nbr_predicted,conf)                    
                    cv2.imshow("you are",facefind)
                    cv2.waitKey(1000)
                except:
                    yes="face not found"
            print yes
            lcd.clear()
            lcd.message(yes)
            time.sleep(5)
	else:
		lcd.clear()
		lcd.message("no intruder \n")
		time.sleep(1)
		continue
