from nanpy import SerialManager, ArduinoApi
from time import sleep
from motors import Motors


connection = SerialManager(device='/dev/ttyUSB0')
try:
	a = ArduinoApi(connection=connection)
except Exception as e:
	print('ERROR CONNECTING TO ARDUINO')
	exit(1)
	
	
motors = Motors()
motors.init_motors(a)

start = input('Any key to start')

print('Right wheel forward')
motors.forward(a, 0, 200)
sleep(1)
print('stopping...')
motors.stop(a)
sleep(.5)
print('Right wheel backward')
motors.reverse(a, 0, 200)
sleep(1)
print('stopping...')
motors.stop(a)
sleep(.5)
start = input('Any key to start')

print('Left wheel forward')
motors.forward(a, 200, 0)
sleep(1)
print('stopping...')
motors.stop(a)
sleep(.5)
print('Left wheel backward')
motors.reverse(a, 200, 0)
sleep(1)
print('stopping...')
motors.stop(a)
sleep(.5)
start = input('any key to start')

print('both wheels forward')
motors.forward(a, 200, 200)
sleep(.5)
print('stopping...')
motors.stop(a)
sleep(.5)
print('both wheels backward')
motors.reverse(a, 200, 200)
sleep(.5)
print('stopping...')
motors.stop(a)
sleep(.5)

while(1):
    start = input('any key to start')
    print('tank turn right')
    motors.drive(a, 200, -200)
    sleep(.5)
    print('stopping...')
    motors.stop(a)
    sleep(.5)
    print('tank turn left')
    motors.drive(a, -200, 200)
    sleep(.5)
    print('stopping...')
    motors.stop(a)
    sleep(.5)




