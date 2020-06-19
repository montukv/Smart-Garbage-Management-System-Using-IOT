#code for testing the  ultrasoinc sensor


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#Defining pins 
TRIG = 4
ECHO = 18
#setup for GPIO input output
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start = time.time()

while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end-start

#CM:
distance = sig_time / 0.000058

#inches:
#distance = sig_time / 0.000148

print('Distance: {} centimeters'.format(distance))

GPIO.cleanup()
