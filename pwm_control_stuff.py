from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)


pwm1 = GPIO.PWM(2,100)

pwm1.start(0)

#while(True):
for i in range(7,10):
    pwm1.ChangeDutyCycle(i*10)
    sleep(2)
    #pwm1.ChangeFrequency(100)
    print(i)
    pwm1.ChangeDutyCycle(0)
    sleep(2)

pwm1.ChangeDutyCycle(0)
pwm1.ChangeFrequency(0)
sleep(3)
pwm1.stop()

GPIO.cleanup()

