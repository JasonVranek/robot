# Camera imports
from __future__ import print_function
import cv2
import imutils
from PiVideoStream import PiVideoStream
from imutils.video.pivideostream import PiVideoStream
# Arduino imports
from nanpy import SerialManager, ArduinoApi
from time import sleep
from motors import Motors
import sys

connection = SerialManager(device='/dev/ttyUSB0')
try:
	a = ArduinoApi(connection=connection)
except Exception as e:
	print('ERROR CONNECTING TO ARDUINO')
	exit(1)
	
	
motors = Motors()
motors.init_motors(a)
print('Initialized Connection to Arduino')

# Initialize the camera thread and allow it time to warmup
camera = PiVideoStream().start()
print('Initialized PiCamera') 
sleep(2.0)

while(True):
	frame = camera.read()
	frame = imutils.resize(frame, width=400)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(30) & 0xFF
	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	#key = input('Move Roboto ')
	#print(key)
	if key == ord('w'):
		print('up')
		motors.forward(a, 200, 200)
		sleep(.5) 
		motors.stop(a)
	elif key == ord('d'):
		print('rotate right')
		motors.drive(a, 200, -200)
		sleep(.5)
		motors.stop(a)
	elif key == ord('a'):
		print('rotate left')
		motors.drive(a, -200, 200)
		sleep(.5)
		motors.stop(a)
	elif key == ord('s'):
		print('down')
		motors.reverse(a, 200, 200)
		sleep(.5)
		motors.stop(a)

camera.stop()




            

