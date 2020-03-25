#!/usr/bin/env python
import datetime
import RPi.GPIO as gpio
import time
import sys
import signal

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

gpio.setmode(gpio.BCM)
trig = [19,6,27] # 7th
echo = [26,13,22] # 6th

for i in range(2):
	gpio.setup(trig[i], gpio.OUT)
	gpio.setup(echo[i], gpio.IN)

time.sleep(0.5)
print ('------------- start')
try :
    while True :
		for i in range(2):
			gpio.output(trig[i], False)
			time.sleep(0.1)
			gpio.output(trig[i], True)
			time.sleep(0.00001)
			gpio.output(trig[i], False)
			while gpio.input(echo[i]) == 0 :
            pulse_start = time.time()
			while gpio.input(echo[i]) == 1 :
            pulse_end = time.time()
			
			pulse_duration = pulse_end - pulse_start
			distance = pulse_duration * 17000
			if distance > 300 or distance==0:
				print('out of range')
				continue
			distance = round(distance, 3)
                        print (datetime.datetime.now())
			print ('Distance',end='')
			print (i,end='')
			print (': %.3f cm'%distance)
			time.sleep(1)
        
except (KeyboardInterrupt, SystemExit):
    gpio.cleanup()
    sys.exit(0)
except:
    gpio.cleanup()
