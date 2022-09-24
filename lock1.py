import RPi.GPIO as GPIO
import time
import signal
import atexit

GPIO.setwarnings(False)
# GPIO.cleanup()
servopin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin,GPIO.OUT,initial=False)
p = GPIO.PWM(servopin,50)

def run(t=1,s=1,a1=4,a2=10):
    p.start(0)
    for i in range(0,t):
        p.ChangeDutyCycle(a1)
        time.sleep(.5)
        p.ChangeDutyCycle(0)
        time.sleep(s)
        p.ChangeDutyCycle(a2)
        time.sleep(.5)
        p.ChangeDutyCycle(0)
        time.sleep(s)
    p.ChangeDutyCycle(0)

def exit():
    GPIO.cleanup()
