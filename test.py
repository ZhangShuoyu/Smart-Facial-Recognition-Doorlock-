import light as li
import time
import RPi.GPIO as GPIO

button = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(16,GPIO.OUT)
#li.lighton()
while True:
    time.sleep(2)
    buttonstate = GPIO.input(button)
    if buttonstate == False:
        #GPIO.output(16,GPIO.HIGH)
        li.lighton()
        break