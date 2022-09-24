from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
 
factory = PiGPIOFactory(host='192.168.1.223')
# myGPIO=17
 
servo = Servo(17, pin_factory=factory)
def runrun():

    i = 1
    while(i<2):
        servo.min()
        sleep(1)
        servo.max()
        sleep(1)
        servo.min()
        sleep(1)
        servo.max()
        sleep(1)
        i = i+1
