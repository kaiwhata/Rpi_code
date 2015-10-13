#Import relevant libraries
from time import sleep
import RPi.GPIO as GPIO

#setup pins on the RPi

GPIO.setmode(GPIO.BCM) #this sets the numbering system.
'''
GPIO.setmode(GPIO.BOARD)
'''
#you can also use GPIO.setmode(BOARD)

#sets individual pins as inputs or outputs
GPIO.setup(2, GPIO.OUT)

pitch = 440 #Hz - change this to change the pitch of your note
time = 1.0/pitch

#we use a for loop to repeat the same action 10 times
for i  in range(1000):
    GPIO.output(2, True) #this sets the voltage on pin 2 to 3.3V
    sleep(time) #wait 1 second before doing anything else

    GPIO.output(2, False) #this sets the voltage on pin 2 to 0V
    sleep(time) #wait 1 second before doing anything else

#this piece of code just makes sure everything is turned off once we finish
GPIO.cleanup()
