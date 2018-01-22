# ImageAnalysis-OpenCV-CloudVision
Image Recognition using OpenCV and performing Image Analysis using Google Cloud Vision API

# Overview
Here is the code for image recognition using OpenCV and Google Cloud Vision API with input from webcam. OpenCV tracks faces and monitors for smiles, when a smile is detected a picture is saved locally on the computer, sent the image to Google Cloud Storage bucket, then Google Cloud Vision API is invoked to analyze that picture, and the results are sent back to console. We need a webcam to provide video input to the program.  

# Dependencies
- Install Ubuntu 16.04, https://www.ubuntu.com/download/desktop
- Install Python 2.7.14, https://www.python.org/downloads/
- Install OpenCV2 with python bindings, http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html
- Intall Google Cloud Python Client, `$ python -m pip install google-cloud`
- Create a Google Cloud Storage Bucket, https://cloud.google.com/vision/docs/quickstart (Note: The bucket needs open write premissions. Make sure to edit the bucket name in the python script)
- Install Google Cloud Storage Python Client, `$ sudo pip install --upgrade google-cloud-storage`
- Install Cloud Vision API Client Libraries, `$ pip install --upgrade google-cloud-vision`
- Authenticating to the Cloud Storage and Vision API, `$ export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE`, https://cloud.google.com/speech/docs/auth#using_a_service_account
- haarcascade_frontalface_default.xml, 
- haarcascade_smile.xml, 
- haarcascade_eye.xml

# Note: 
Ubuntu 16.04 actually ships out-of-the-box with both Python 2.7 and Python 3.5 installed. The actual versions are:
 1. Python 2.7.12 (used by default when you type python in your terminal).
 2. Python 3.5.2 (can be accessed via the python3 command).
    
Make sure to create virtual environment for Python 2 while installing OpenCV. Virtualenv is a tool to create isolated Python environments. Refer: http://pythonopencv.com/install-opencv-3-3-and-python2-7-3-5-bindings-on-ubuntu-16-04/, https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

If you face isssues while installing OpenCV or running the program, try re-installing OpenCV 'WITH_JPEG=OFF' in CMAKE command this time.


# Usage
Run following code in the terminal,

`python imagerecog-opencv-cloudvision.py`

# References
https://cloud.google.com/vision/docs/
https://cloud.google.com/python/
https://cloud.google.com/vision/docs/reference/libraries

Enjoy, Have Fun!

