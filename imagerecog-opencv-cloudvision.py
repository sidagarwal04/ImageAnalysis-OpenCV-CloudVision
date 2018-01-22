import cv2
import numpy as np
import sys
import io
import os
import google.cloud.storage
import google.cloud.vision

sys.path.append('/usr/local/lib/python2.7/site-packages/')

# Create a storage client.
storage_client = google.cloud.storage.Client()

# TODO (Developer): Replace this with your Cloud Storage bucket name.
bucket_name = 'Enter Google Cloud Storage Bucket Name here'
bucket = storage_client.get_bucket(bucket_name)

facePath = "./haarcascade_frontalface_default.xml"
smilePath = "./haarcascade_smile.xml"
eyePath = "./haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)
eyeCascade = cv2.CascadeClassifier(eyePath)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05

is_looping = True

while True:

    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= sF,
        minNeighbors=8,
        minSize=(55, 55)
    )
	
  # ---- Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
	
    # ---- Draw a rectangle around the eyes
    eyes = eyeCascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25)
            )


        # Set region of interest for smiles
        for (x, y, w, h) in smile:

           print "Found", len(smile), "smiles!"
           cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
	   cv2.imwrite('smile_image.png', gray)
	   
	   # Upload the captured picture to Google Cloud Storage
	   # TODO (Developer): Replace this with the name of the local file to upload.
	   source_file_name = 'smile_image.png'
       blob = bucket.blob(os.path.basename(source_file_name))

       # Upload the local file to Cloud Storage.
       blob.upload_from_filename(source_file_name)
	   print('File {} uploaded to {}.'.format(source_file_name,bucket))
	   
	   # TODO (Developer): Replace this with the name of the file to be downloaded locally.
	   source_file_name = 'smile_image.png'
	   blob = bucket.blob(source_file_name)
	   destination_file_name= 'smile_image_downloaded.png'
		
	   # Download the uploaded file from Cloud Storage.
	   blob.download_to_filename(destination_file_name)
	   print('Blob {} downloaded from {}.'.format(destination_file_name, bucket))

	   # Create a Vision client.
	   vision_client = google.cloud.vision.ImageAnnotatorClient()

	   # TODO (Developer): Replace this with the name of the local image
	   # file to analyze.	
	   fileName=destination_file_name
	   with io.open(fileName, 'rb') as image_file:
	   	content = image_file.read()

        # Use Vision to label the image based on content.
		image = google.cloud.vision.types.Image(content=content)
		response = vision_client.label_detection(image=image)

	   print('Labels:')
	   for label in response.label_annotations:
	   		print(label.description)
		   
	   cv2.waitKey(0)

    # Look at the Camera, Press ESC to capture a selfie
    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
	break

    if not is_looping:
	cv2.waitKey(0)
	print "Found Smile"
	break

cap.release()
cv2.destroyAllWindows()                
                
