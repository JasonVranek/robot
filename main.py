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
        motors.forward(a, 100, 100)

    elif key == '\x1b[B':
        print('down')
        motors.reverse(a, 100, 100)
    else:
        print('quitting...')
        motors.stop(a)



            

