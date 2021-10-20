import RPi.GPIO as GPIO
import json
import time
GPIO.setmode(GPIO.BCM)

ledPinA = 4 # First LED GPIO Pin
ledPinB = 5 # Second LED GPIO Pin
ledPinC = 6 # Third LED GPIO Pin


GPIO.setup(ledPinA, GPIO.OUT)
GPIO.setup(ledPinB, GPIO.OUT)
GPIO.setup(ledPinC, GPIO.OUT)

pwmA = GPIO.PWM(ledPinA, 100) # PWM object on our pin at 100 Hz
pwmB = GPIO.PWM(ledPinB, 100) # PWM object on our pin at 100 Hz
pwmC = GPIO.PWM(ledPinC, 100) # PWM object on our pin at 100 Hz

pwmA.start(0) # start with LED A off
pwmB.start(0) # start with LED B off
pwmC.start(0) # start with LED C off
while True:
  with open("lab4_CGI.txt", 'r') as f:
    data = json.load(f)
  slider = 
  time.sleep(0.1) 