import cv
import cv2
import numpy as np
import time
import video
import sys

# temporary hardcoded video sources
camLeft = 3
camRight = 4

def write_jpeg(fn, img):
    #fullFn = '/images/' + fn
    cv.SaveImage(fn, cv.fromarray(img))

if __name__ == '__main__':
    print __doc__
    
    def nothing(*arg):
        pass

    # create windows
    cv2.namedWindow('camLeft')
    cv2.namedWindow('camRight')
    
    #set up video captures
    capL = video.create_capture(camLeft)
    capR = video.create_capture(camRight)
    
    #cv2.waitKey()
    #time.sleep(6)
    
    count = 0
    
    while True:
    	print 'top of capture loop'
    	
    	count += 1
    	
    	#get video frames
        flagL, imgL = capL.read()
        flagR, imgR = capR.read()
        
        #display images
        cv2.imshow('camLeft', imgL)
        cv2.imshow('camRight', imgR)
        
        # generate filenames
        left_fn = 'left' + str(count) + '.jpeg'
        right_fn = 'right' + str(count) + '.jpeg'
        
        # write files
        write_jpeg(left_fn, imgL)
        print '%s saved' % left_fn
        write_jpeg(right_fn, imgL)
        print '%s saved' % right_fn
        
        # detect keypresses
        ch = cv2.waitKey(5)
        if ch == 27:
            # exit on 'escape' key
            break
            
        time.sleep(1)
    cv2.destroyAllWindows() 			

