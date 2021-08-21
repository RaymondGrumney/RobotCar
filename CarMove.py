#!/usr/bin/python3

# Import required modules
import time
import RPi.GPIO as GPIO
from Pinout import *

class CarMove:
  pins = Pinout()
  PMWA = pins.PMWA
  AIN2 = pins.AIN2
  AIN1 = pins.AIN1
  BIN1 = pins.BIN1
  BIN2 = pins.BIN2
  PMWB = pins.PMWB
  STBY = pins.STBY
  _speed=100     # Speed of drive motors
  _control=100   # speed of steering motor

  def _set_speed(self,percentage):
    SPEEDA.ChangeDutyCycle(percentage)
    self._speed=percentage
  def _get_speed(self):
    return self._speed
  speed=property(_get_speed, _set_speed)

  def _set_control(self,percentage):
    SPEEDB.ChangeDutyCycle(percentage)
    self._control=percentage
  def _get_control(self):
    return self._control
  control=property(_get_control, _set_control)

  def setup(self):
    print("Setting up GPIOs")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.PMWA, GPIO.OUT)
    global SPEEDA
    SPEEDA=GPIO.PWM(self.PMWA,self._speed)
    SPEEDA.start(self._speed)
    GPIO.setup(self.AIN2, GPIO.OUT)
    GPIO.setup(self.AIN1, GPIO.OUT)
    GPIO.setup(self.STBY, GPIO.OUT)
    GPIO.setup(self.BIN1, GPIO.OUT)
    GPIO.setup(self.BIN2, GPIO.OUT)
    GPIO.setup(self.PMWB, GPIO.OUT)
    global SPEEDB
    SPEEDB=GPIO.PWM(self.PMWB,self._control)
    SPEEDB.start(self._control)
    self.stop()

  def forward(self):
    GPIO.output(self.AIN1, GPIO.HIGH)
    GPIO.output(self.AIN2, GPIO.LOW)
    GPIO.output(self.PMWA, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def backward(self):
    GPIO.output(self.AIN1, GPIO.LOW)
    GPIO.output(self.AIN2, GPIO.HIGH)
    GPIO.output(self.PMWA, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def stop(self):
    GPIO.output(self.AIN1, GPIO.LOW)
    GPIO.output(self.AIN2, GPIO.LOW)
    GPIO.output(self.PMWA, GPIO.LOW)
    GPIO.output(self.STBY, GPIO.LOW)
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.LOW)


  def left(self):
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)
    GPIO.output(self.PMWB, GPIO.HIGH)

  def right(self):
    GPIO.output(self.BIN1, GPIO.HIGH)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def __init__(self):
    self.setup()
    self.stop()

  def __del__(self):
    GPIO.cleanup()
