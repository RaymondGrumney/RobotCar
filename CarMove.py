#!/usr/bin/python3

# Import required modules
import time
import RPi.GPIO as GPIO


class CarMove:
  PMWA=7
  AIN2=11
  AIN1=12
  BIN1=15
  BIN2=16
  PMWB=18
  STBY=13

  def setup(self):
    print("Setting up GPIOs")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.PMWA, GPIO.OUT) # Connected to PWMA
    global SPEEDA
    SPEEDA=GPIO.PWM(self.PMWA,100)
    SPEEDA.start(100)
    GPIO.setup(self.AIN2, GPIO.OUT) # Connected to AIN2
    GPIO.setup(self.AIN1, GPIO.OUT) # Connected to AIN1
    GPIO.setup(self.STBY, GPIO.OUT) # Connected to STBY
    GPIO.setup(self.BIN1, GPIO.OUT) # Connected to BIN1
    GPIO.setup(self.BIN2, GPIO.OUT) # Connected to BIN2
    GPIO.setup(self.PMWB, GPIO.OUT) # Connected to PWMV
    global SPEEDB
    SPEEDB=GPIO.PWM(self.PMWB,100)
    SPEEDB.start(100)
    self.stop()

  def forward(self):
    print("Forward")
    # Drive the motor clockwise
    GPIO.output(self.AIN1, GPIO.HIGH)
    GPIO.output(self.AIN2, GPIO.LOW)
    GPIO.output(self.PMWA, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def backward(self):
    # Drive the motor counterclockwise
    GPIO.output(self.AIN1, GPIO.LOW) # Set AIN1
    GPIO.output(self.AIN2, GPIO.HIGH) # Set AIN2
    GPIO.output(self.PMWA, GPIO.HIGH) # Set PWMA
    GPIO.output(self.STBY, GPIO.HIGH)

  def stop(self):
    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(self.AIN1, GPIO.LOW) # Set AIN1
    GPIO.output(self.AIN2, GPIO.LOW) # Set AIN2
    GPIO.output(self.PMWA, GPIO.LOW)  # Set PWMA
    GPIO.output(self.STBY, GPIO.LOW) # Set STBY
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.LOW)


  def left(self):
    print("Left")
    GPIO.output(self.BIN1, GPIO.LOW)
    GPIO.output(self.BIN2, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)
    GPIO.output(self.PMWB, GPIO.HIGH)

  def right(self):
    print("Right")
    GPIO.output(self.BIN1, GPIO.HIGH)
    GPIO.output(self.BIN2, GPIO.LOW)
    GPIO.output(self.PMWB, GPIO.HIGH)
    GPIO.output(self.STBY, GPIO.HIGH)

  def speedSet(self,percentage):
    SPEEDA.ChangeDutyCycle(percentage)

  def __init__(self):
    self.setup()
    self.stop()

  def cleanup(self):
    GPIO.cleanup()

#def main():
 # setup()
  #stop()

  #forward()
  #time.sleep(0.5)
#  backward()
  #speedSet(70)
  #time.sleep(0.5)
  #speedSet(55)
#  stop()
  #time.sleep(0.5)
  #right()
  #time.sleep(0.5)
  #left()
  #time.sleep(0.5)
 # stop()

  # Exitting
  #cleanup()

#if __name__ == "__main__":
 # main()

