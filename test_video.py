from __future__ import print_function
import cv2
import imutils
import time
from PiVideoStream import PiVideoStream
from imutils.video.pivideostream import PiVideoStream
from collections import deque
import numpy as np

# lower and upper boundaries of the "green" in HSV
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
#buffer = 64
# initialize the list of tracked points, to draw the ball trayectory
#pts = deque(64)
#resolution=(64,64)255 8 127
pink = (127, 8, 255)
# Pinks HSV in CV2 is H=165 S=96.9%, V=100%
pink_max = np.array([180, 255, 255], np.uint8)
pink_min = np.array([165, 50, 50], np.uint8)
THICKNESS = -1
camera = PiVideoStream().start()
time.sleep(2.0)
i=100000
while(i):
	frame = camera.read()
	#frame = imutils.resize(frame, width=400)
	
	# resize the frame, blur it, and convert it to the HSV color space
	#rame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				pink, THICKNESS)
			#cv2.circle(frame, center, 5, (0, 0, 255), -1)
			
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, pink_min, pink_max)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
	
	
	#cv2.imshow("Frame", frame)
	cv2.imshow("Mask", mask)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
	i-=1
camera.stop()






print('done')

