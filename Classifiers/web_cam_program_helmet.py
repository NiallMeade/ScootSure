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

avg_color = [0,0,0]
#deep neaural net model for face recognition
prototxt = './deploy.prototxt.txt'
model = './res10_300x300_ssd_iter_140000.caffemodel'
confidence_threshold = 0.6

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
	# grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 165.0))

	# pass the blob through the network and obtain the detections and
	# predictions
    net.setInput(blob)
    detections = net.forward()

   

    # loop over the detections
    for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
        confidence = detections[0, 0, i, 2]
 
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
        if confidence < confidence_threshold:
            continue
 
		# compute the (x, y)-coordinates of the bounding box for the
		# object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        h_ = endY-startY
        w_ = endX-startX

        #get the top of the head
        endY = endY - int((h_)/1.1)
        startY = startY - int((h_)/3)
        startX = startX - int((w_)/10)
        endX = endX + int((w_)/10)

        #crop the top of the head
        try:
            cropped = frame[startY:endY, startX:endX]
            avg_color_per_row = numpy.average(cropped, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            print(avg_color)
        except:
            print("whoops")

        #check if red intensity is above threshold (for helmet)
        if(avg_color[2]>120):
            text = "Wearing Helmet"
            col = (0,255,0)
        else:
            text = "No Helmet"
            col = (0,0,255)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        #draw the bounding box 
        cv2.rectangle(frame, (startX, startY), (endX, endY),
            col, 2)
        
       
    #show the output frame    
    try:
        frame = cv2.flip(frame,1)
        if startX > w/2:
            pos = int(w/2) - (startX - int(w/2))
        else:
            pos = int(w/2) + (int(w/2) - startX)
        cv2.putText(frame, text, (pos-(endX-startX), y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, col, 2)
        #frame = cv2.resize(frame, (w*3,h*3))
        cv2.imshow("Helmet Classifier", frame)
    except:
        cv2.imshow("Helmet Classifier", frame)
        
    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
