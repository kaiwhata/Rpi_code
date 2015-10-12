from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

while(True):
    print "Led off\n"
    GPIO.output(2, False)
    sleep(0.75)

    print "Led on\n"
    GPIO.output(2, True)
    sleep(0.25)

