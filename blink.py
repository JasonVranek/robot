from nanpy import SerialManager, ArduinoApi
from time import sleep
connection = SerialManager(device='/dev/ttyUSB0')

a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
while True:
    a.digitalWrite(13, a.HIGH)
    sleep(.5)
    a.digitalWrite(13, a.LOW)
    sleep(.5)
    pass
