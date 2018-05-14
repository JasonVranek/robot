from nanpy import SerialManager, ArduinoApi
from time import sleep
from ping_sensors import PingSensor


connection = SerialManager(device='/dev/ttyUSB0')
try:
	a = ArduinoApi(connection=connection)
except Exception as e:
	print('ERROR CONNECTING TO ARDUINO')
	exit(1)
	
# right motor
echo = 'A0'
trigger = 'A1'

# left motor
#enc_al = 'A6'
#enc_bl = 'A7'
ping = PingSensor(a,trigger,echo).start()

i=10000
while i:
        print(ping.read())
        sleep(.1)
print(done)
