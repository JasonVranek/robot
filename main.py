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

while True:
    motors.forward(a, 100, 100)
    sleep(1)
    motors.reverse(a, 100, 100)
    sleep(1)


            

