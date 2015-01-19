#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

button_previous = 1
button_current = 1
brojac = 0
flag_pressed = 0

while True:

  button_current = GPIO.input(17);
  flag_pressed = button_previous + button_current

  if (not(flag_pressed)):
    brojac += 1
  else:
    brojac = 0

  if (button_current and (not button_previous)):
    #print("Reset")  
    os.system("sudo shutdown -r now")
  if ((not flag_pressed) and  brojac >= 100):
    #print("Shutdown")
    os.system("sudo shutdown -h now")
    break
  
  button_previous = button_current
  time.sleep(0.03)

