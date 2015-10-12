#Import relevant libraries
from time import sleep
import RPi.GPIO as GPIO

#setup pins on the RPi
GPIO.setmode(GPIO.BCM) #this sets the numbering system.
#you can also use GPIO.setmode(BOARD)

#sets individual pins as inputs or outputs
GPIO.setup(2, GPIO.OUT)

pitches = [440, 493, 523, 587, 659, 698, 783, 880] #Hz - change this to change the pitch of your note
times = [1.0/i for i in pitches]

for t in times:
    #we use a for loop to repeat the same action 1000 times
    for i  in range(100):
        GPIO.output(2, True) #this sets the voltage on pin 2 to 3.3V
        sleep(t) #wait 1 second before doing anything else

        GPIO.output(2, False) #this sets the voltage on pin 2 to 0V
        sleep(t) #wait 1 second before doing anything else

for t in reversed(times):
    #we use a for loop to repeat the same action 1000 times
    for i  in range(100):
        GPIO.output(2, True) #this sets the voltage on pin 2 to 3.3V
        sleep(t) #wait 1 second before doing anything else

        GPIO.output(2, False) #this sets the voltage on pin 2 to 0V
        sleep(t) #wait 1 second before doing anything else

#this piece of code just makes sure everything is turned off once we finish
GPIO.cleanup()
