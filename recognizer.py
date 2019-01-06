import cv, os
from PIL import Image
import numpy as np

def recog(path,faceCascade,recognizer):
    Newimage_paths=[os.path.join(path,f) for f in os.listdir(path)]
    for image_path in Newimage_paths:
    	predict_image_pil = Image.open(image_path).convert('L')
        predict_image = np.array(predict_image_pil, 'uint8')
    	faces = faceCascade.detectMultiScale(predict_image)
    	for (x, y, w, h) in faces:
        	nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
	return nbr_predicted, conf
