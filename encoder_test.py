from nanpy import SerialManager, ArduinoApi
from time import sleep
from motors import Motors


connection = SerialManager(device='/dev/ttyUSB0')
try:
	a = ArduinoApi(connection=connection)
except Exception as e:
	print('ERROR CONNECTING TO ARDUINO')
	exit(1)
	
# right motor
enc_ar = 'A0'
enc_br = 'A1'

# left motor
enc_al = 'A6'
enc_bl = 'A7'
	
# Make pins digital inputs
a.pinMode(enc_ar, a.INPUT)
a.pinMode(enc_br, a.INPUT)
a.pinMode(enc_al, a.INPUT)
a.pinMode(enc_bl, a.INPUT)
last_enc_al = a.LOW
last_enc_bl = a.LOW

while True:
	read_a = a.digitalRead(enc_al)
	read_b = a.digitalRead(enc_bl)
	print(read_a, read_b)
	'''
	if last_enc_al != read_a:
		print('Left encA change')
		print(read_a, read_b)
	if last_enc_bl != read_b:
		print('Left encA change')
		print(read_a,read_b)
	last_enc_al = read_a
	last_enc_bl = read_b
	'''
	sleep(.0001)
	#if last_enc_al is a.LOW and read_a is a.HIGH:	
	#	print('yipeee')
	#	break
	#sleep(.1)

'''
n = digitalRead(encoder0PinA);
  if ((encoder0PinALast == LOW) && (n == HIGH)) {
    if (digitalRead(encoder0PinB) == LOW) {
      encoder0Pos--;
    } else {
      encoder0Pos++;
    }
    Serial.print (encoder0Pos);
    Serial.print ("/");
  }
  encoder0PinALast = n;
'''
