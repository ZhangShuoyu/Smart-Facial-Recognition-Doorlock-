import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# GPIO.cleanup()
inpin = 15
outpin = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outpin,GPIO.OUT)
GPIO.setup(inpin,GPIO.IN)

# try:
def lighton():
    i = 1
    while True:
        inpin = 15
        outpin = 16
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(outpin,GPIO.OUT)
        GPIO.setup(inpin,GPIO.IN)
        i = i+1
        if GPIO.input(inpin) == True:
            GPIO.output(outpin,GPIO.HIGH)
            time.sleep(3)
        else:
            GPIO.output(outpin,GPIO.LOW)
        print(i)
        if i>1000:
            break
def exit():
    GPIO.cleanup()
           