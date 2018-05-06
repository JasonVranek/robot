class Motors(object):
    def __init__(self):
        self.enA = 10
        self.in1 = 8#9
        self.in2 = 9#8
        self.enB = 5
        self.in3 = 7
        self.in4 = 6
		
    def init_motors(self, a):
        a.pinMode(self.enA, a.OUTPUT)
        a.pinMode(self.enB, a.OUTPUT)
        a.pinMode(self.in1, a.OUTPUT)
        a.pinMode(self.in2, a.OUTPUT)
        a.pinMode(self.in3, a.OUTPUT)
        a.pinMode(self.in4, a.OUTPUT)


    def reverse(self, a, left, right):
        # turn on motor A
        a.digitalWrite(self.in1, a.HIGH)
        a.digitalWrite(self.in2, a.LOW)
        # pwm is limited to 0-255
        if(left > 255):
            left = 255
        if(left < 0):
            left = 0

        # turn on motor B
        a.digitalWrite(self.in3, a.HIGH)
        a.digitalWrite(self.in4, a.LOW)
        # pwm is limited to 0-255
        if right > 255:
            right = 255
        if left < 0:
            left = 0

        a.analogWrite(self.enA, left)
        a.analogWrite(self.enB, right)


    def forward(self, a, left, right):
        # turn on motor A
        a.digitalWrite(self.in1, a.LOW)
        a.digitalWrite(self.in2, a.HIGH)
        if left > 255:
            left = 255
        if left < 0:
            left = 0
        
        # turon on motor B
        a.digitalWrite(self.in3, a.LOW)
        a.digitalWrite(self.in4, a.HIGH)
        if right > 255:
            right = 255
        if right < 0:
            left = 0

        a.analogWrite(self.enA, left)
        a.analogWrite(self.enB, right)


    def drive(self, a, left, right):
        if left >= 0:
            if left > 255:
                left = 255		    
            # drive the left motor forward
            a.digitalWrite(self.in1, a.HIGH)
            a.digitalWrite(self.in2, a.LOW)

        if left < 0:
            if left < -255:
                left = 0
            # drive the left motor backwards
            a.digitalWrite(self.in1, a.LOW)
            a.digitalWrite(self.in2, a.HIGH)
        
        if right >= 0:
            if right > 255:
                right = 255
            # driver the right motor forward
            a.digitalWrite(self.in3, a.LOW)
            a.digitalWrite(self.in4, a.HIGH)

        if right < 0:
            if right < -255:
                right = 0
            # drive the right motor backwards
            a.digitalWrite(self.in3, a.HIGH)
            a.digitalWrite(self.in4, a.LOW)

        # write the pwms
        a.analogWrite(self.enA, abs(left))
        a.analogWrite(self.enB, abs(right))


    def stop(self, a):
        a.digitalWrite(self.in1, a.LOW)
        a.digitalWrite(self.in2, a.LOW)
        a.digitalWrite(self.in3, a.LOW)
        a.digitalWrite(self.in4, a.LOW)
	




if __name__ == '__main__':
    test = Motors()