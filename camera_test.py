from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.resolution = (64,64)
camera.capture('test.jpeg')
camera.stop_preview()
