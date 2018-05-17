from time import sleep, time
from threading import Thread

class PingSensor(object):
        def __init__(self, a, trig, echo):
                self.a = a
                self.echo = echo
                self.trig = trig
                self.stopped = False
                self.distance = 0 
                
        def init_ping(self):
                self.a.pinMode(self.trig, a.OUTPUT)
                self.a.pinMode(self.echo, a.INPUT)

        def read(self):
                return self.distance
        
        def start(self):
                Thread(target=self.update, args=()).start()
                return self
	
        def stop(self):
                self.stopped = True
                
        def update(self):
                a = self.a
                if self.stopped:
                        return
                
                # trig high for 10 us
                a.digitalWrite(self.trig, a.HIGH)
                sleep(.00001)

                # turn off trigger and start timers
                a.digitalWrite(self.trig, a.LOW)
                start_time = time()
                stop_time = start_time

                while not a.digitalRead(self.echo):
                        start_time = time()
                while a.digitalRead(self.echo):
                      stop_time = time()

                delta_t = stop_time - start_time
                # distance in cm
                self.distance = float(delta_t*34300)/2
                      
		

