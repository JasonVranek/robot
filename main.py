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

while(True):
    key = input('Move Roboto ')
    print(key)
    if key == '\x1b[A':
        print('up')
        motors.forward(a, 200, 200)
        sleep(.5) 
        motors.stop(a)
    elif key == '\x1b[C':
        print('rotate right')
        motors.drive(a, 200, -200)
        sleep(.5)
        motors.stop(a)
    elif key == '\x1b[D':
        print('rotate left')
        motors.drive(a, -200, 200)
        sleep(.5)
        motors.stop(a)
    elif key == '\x1b[B':
        print('down')
        motors.reverse(a, 200, 200)
        sleep(.5)
        motors.stop(a)
    else:
        print('quitting...')
        motors.stop(a)
        break




            

