# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
from matplotlib import pyplot as plt
import imutils
import time
from PIL import Image
import cv2
import numpy
from keras.models import load_model


# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

IMG_W = 50
IMG_H = 50
#terrain_model = load_model('terrain_model.h5')
terrain_model = load_model('terrain_model.h5', compile=False)
terrain_classes=['Curb', 'Footpath', 'Grass', 'Stones', 'Road', 'Sand', 'Snow', 'Wet'] 

def classify_image(pic):
    
    pic = cv2.resize(pic, (IMG_W, IMG_H))
    pic = np.expand_dims(pic, axis=0)
    class_predicted = terrain_model.predict_classes(pic)
    return class_predicted.max()

# loop over the frames from the video stream
while True:

    frame = vs.read()
    (h, w) = frame.shape[:2]
    frame = imutils.resize(frame, width=400)
    pred = classify_image(frame)
    frame = cv2.flip(frame,1)
    prediction = terrain_classes[pred]
    cv2.putText(frame, prediction, (20, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    cv2.imshow("Terrain Classifier", frame)
        
    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
