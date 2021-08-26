#!/usr/bin/python3

# Import required modules
import time
import RPi.GPIO as GPIO
from Pinout import *

class CarMoveTankSteering:
  pins = Pinout()
  PMWA = pins.PMWA
  AIN2 = pins.AIN2
  AIN1 = pins.AIN1
  BIN1 = pins.BIN1
  BIN2 = pins.BIN2
  PMWB = pins.PMWB
  STBY = pins.STBY
  _Aspeed=100     # Speed of drive motors
  _Bspeed=100   # speed of steering motor

  def _set_a_speed(self,percentage):
    SPEEDA.ChangeDutyCycle(percentage)
    self._Aspeed=percentage
  def _get_a_speed(self):
    return self._Aspeed
  a_speed=property(_get_a_speed, _set_a_speed)

  def _set_b_speed(self,percentage):
    SPEEDB.ChangeDutyCycle(percentage)
    self._Bspeed=percentage
  def _get_b_speed(self):
    return self._Bspeed
  b_speed=property(_get_b_speed, _set_b_speed)

  def setup(self):
    print("Setting up GPIOs")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.PMWA, GPIO.OUT)
    global SPEEDA
    SPEEDA=GPIO.PWM(self.PMWA,self._Aspeed)
    SPEEDA.start(self._Aspeed)
    GPIO.setup(self.AIN2, GPIO.OUT)
    GPIO.setup(self.AIN1, GPIO.OUT)
    GPIO.setup(self.STBY, GPIO.OUT)
    GPIO.setup(self.BIN1, GPIO.OUT)
    GPIO.setup(self.BIN2, GPIO.OUT)
    GPIO.setup(self.PMWB, GPIO.OUT)
    global SPEEDB
    SPEEDB=GPIO.PWM(self.PMWB,self._Bspeed)
    SPEEDB.start(self._Bspeed)
    self.stop()


  def a_forward(self):
    GPIO.output(self.AIN1, GPIO.HIGH)
    GPIO.output(self.AIN2, GPIO.LOW)
    GPIO.output(self.PMWA, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def a_backward(self):
    GPIO.output(self.AIN1, GPIO.LOW)
    GPIO.output(self.AIN2, GPIO.HIGH)
    GPIO.output(self.PMWA, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)


  def b_forward(self):
    GPIO.output(self.BIN1, GPIO.HIGH)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def b_backward(self):
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)
    GPIO.output(self.PMWB, GPIO.HIGH)


  def a_stop(self):
    GPIO.output(self.AIN1, GPIO.LOW)
    GPIO.output(self.AIN2, GPIO.LOW)
    GPIO.output(self.PMWA, GPIO.LOW)

  def b_stop(self):
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.LOW)

  def stop(self):
    self.a_stop()
    self.b_stop()


  def __init__(self):
    self.setup()
    self.stop()

  def __del__(self):
    GPIO.cleanup()
