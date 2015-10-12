#Import relevant libraries
from time import sleep
import RPi.GPIO as GPIO

#setup pins on the RPi
GPIO.setmode(GPIO.BCM) #this sets the numbering system.
#you can also use GPIO.setmode(BOARD)

#sets individual pins as inputs or outputs
GPIO.setup(2, GPIO.OUT)

#we use a for loop to repeat the same action 10 times
for i  in range(10):
    print('On') #this print command just reports what's going on in the console
    GPIO.output(2, True) #this sets the voltage on pin 2 to 3.3V
    sleep(1) #wait 1 second before doing anything else

    print('Off') 
    GPIO.output(2, False) #this sets the voltage on pin 2 to 0V
    sleep(1) #wait 1 second before doing anything else

#this piece of code just makes sure everything is turned off once we finish
GPIO.cleanup()
