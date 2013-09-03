'''
This is a heavily modified version of an openCV sample demonstrating
Canny edge detection. It no longer does Canny edge detection.
I used it mostly for it's HighGUI code.

Usage:
  pyFaceDetect.py [no args]

  Runtime arguments and trackbars no longer exist.

'''

# TODO:


import cv2
import numpy as np
import time
import video
import sys

# temporary hardcoded video sources
camLeft = 3
camRight = 4

# improve tracking
goodPoints = list()

def detect(img, cascade_fn='haarcascade_frontalface_alt.xml',
	scaleFactor=1.3, minNeighbors=4, minSize=(20, 20),
	flags=cv2.cv.CV_HAAR_SCALE_IMAGE):
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	
	cascade = cv2.CascadeClassifier(cascade_fn)
	faces = list()
	rect = cascade.detectMultiScale(gray, scaleFactor=scaleFactor,
	minNeighbors=minNeighbors, minSize=minSize, flags=flags)
	
	for x1, y1, x2, y2 in rect:
		faces.append([y1, y2, x1, x2])
		
		if len(faces) == 1:
			goodPoints.append([y1, y2, x1, x2])
		if len(goodPoints) >= 3:
			data1 = goodPoints[0]
			data2 = goodPoints[1]
			data3 = goodPoints[2]
			
			avgX = (data1[2] + data2[2] + data3[2]) / 3
			avgY = (data1[0] + data2[0] + data3[0]) / 3
			avgW = (data1[3] + data2[3] + data3[3]) / 3
			avgH = (data1[1] + data2[1] + data3[1]) / 3
			
			cv2.rectangle(img, (avgX, avgY), (avgX+avgW, avgY+avgH), (0, 0, 255), 3)
			
			pop1 = goodPoints.pop(0)
		
	return faces, img

if __name__ == '__main__':
	print __doc__
    
	def nothing(*arg):
		pass

    # create windows
	cv2.namedWindow('camInput')
	cv2.namedWindow('camFaces')
    #cv2.namedWindow('tools')
    
    # create trackbar tools
    #cv2.createTrackbar('uniqRat', 'tools', 10, 20, nothing)

    #set up video capture
	capL = video.create_capture(camLeft)
    
    #cv2.waitKey()
    #time.sleep(6)
    
	while True:
		print 'top of capture/compute loop'
		
		#get video frames
		print 'capture'
		flagL, imgL = capL.read()
        
        #display images
		print 'display'
		cv2.imshow('camInput', imgL)
        
        # downscale images for faster processing
		print 'downscale'
		imgLds = cv2.pyrDown( imgL )
		
		# detect faces
		print 'detect faces'
		faces, imgFaces = detect(imgLds)
		print 'found: ' + str(len(faces))
		
		# show detected
		print 'show detected faces'
		cv2.imshow('camFaces', imgFaces)
		for face in faces:
			print face
		
        # detect keypresses
		ch = cv2.waitKey(5)
		if ch == 27:
			# exit on 'escape' key
			break
		
		print 'bottom of loop\n'
		
	cv2.destroyAllWindows() 			

