import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
mode=GPIO.getmode()

GPIO.cleanup()

Forward=26
Backward=24
Pwm = 33
Forward1=21
Backward1=23
Pwm1 = 32

weeder = 7
cutter = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(weeder, GPIO.OUT)
GPIO.setup(cutter, GPIO.OUT)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Pwm,GPIO.OUT)
GPIO.setup(Forward1, GPIO.OUT)
GPIO.setup(Backward1, GPIO.OUT)
GPIO.setup(Pwm1,GPIO.OUT)
GPIO.output(weeder, GPIO.LOW)
GPIO.output(cutter, GPIO.LOW)
R = GPIO.PWM(Pwm,1000)
L = GPIO.PWM(Pwm1,1000)

R.start(0)
L.start(0)
def cutOff():
    GPIO.output(cutter, GPIO.LOW)
def cutOn():
    GPIO.output(cutter, GPIO.HIGH)
def weedOff():
    GPIO.output(weeder, GPIO.LOW)
def weedOn():
    GPIO.output(weeder, GPIO.HIGH)
def stop():
    GPIO.output(Backward, GPIO.LOW)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward1, GPIO.LOW)
    GPIO.output(Forward1, GPIO.LOW)
    R.ChangeDutyCycle(0)
    L.ChangeDutyCycle(0)
    print("working")
    

def forward(speed = 100):
    stop()
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Forward1, GPIO.HIGH)
    R.ChangeDutyCycle(speed)
    L.ChangeDutyCycle(speed)
    #print("Moving forward")


def reverse(speed = 100):
    stop()
    GPIO.output(Backward, GPIO.HIGH)
    GPIO.output(Backward1, GPIO.HIGH)
    R.ChangeDutyCycle(speed)
    L.ChangeDutyCycle(speed)
    #print("Moving backward")
    
def Right():
    GPIO.output(Backward, GPIO.HIGH)
    GPIO.output(Backward1, GPIO.HIGH)
    R.ChangeDutyCycle(75)
    L.ChangeDutyCycle(100)
    
def Left():
    GPIO.output(Backward, GPIO.HIGH)
    GPIO.output(Backward1, GPIO.HIGH)
    R.ChangeDutyCycle(100)
    L.ChangeDutyCycle(75)
    
#forward(100)
#reverse(100)
# Right(100):
def Drive(cmd,speed = 100):
    print(cmd)
    if(cmd == "CS"):
        cutOff()
    if(cmd == "C"):
        cutOn()
    if(cmd == "WS"):
        weedOff()
    if(cmd == "W"):
        weedOn()
    if(cmd == "S"):
        stop()
    if(cmd == 'RV'):
        reverse(speed)
    if(cmd == 'F'):
        forward(speed)
    if(cmd == 'L'):
        Left()
    if(cmd == 'R'):
        Right()
        
Drive("S",100)