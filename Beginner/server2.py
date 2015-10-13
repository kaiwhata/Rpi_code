#import the relevant libraries 
from bottle import route, run
from time import sleep
import RPi.GPIO as GPIO


#when you visit the website's homepage...
@route('/')
def homepage():
    #display the words "Hello user"
    return "Hello User!"

#when you visit the website URL +/name/jimmy...
@route('/note/<pitch>')
def playnote(pitch):

    time = 1.0/float(pitch)

    for i  in range(1000):
        GPIO.output(2, True) #this sets the voltage on pin 2 to 3.3V
        sleep(time) #wait 1 second before doing anything else

        GPIO.output(2, False) #this sets the voltage on pin 2 to 0V
        sleep(time) #wait 1 second before doing anything else
        
    #display the words "Hello " plus the name they typed in the URL i.e. jimmy
    return "Playing "+str(pitch)+" Hz!"


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

#this is where we run the server and tell it where to listen\
#'0.0.0.0' means listens to all incoming signals on port 8080
run(host='0.0.0.0', port=8080, reloader=True)
