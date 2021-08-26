#!/bin/python3
import pygame
from CarMoveTankSteering import *

XBOXONE_JOYPAD=1536
LEFT_AXIS=1
RIGHT_AXIS=3

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

c=CarMoveTankSteering()

while keepPlaying:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == XBOXONE_JOYPAD:
      if event.axis == RIGHT_AXIS:
        c.a_speed=int(abs(event.value) * 92)
        if event.value > 0:
          c.a_forward()
        elif event.value < 0:
          c.a_backward()
        else:
          c.a_stop()
      if event.axis == LEFT_AXIS:
        c.b_speed = int(abs(event.value) * 99)
        if event.value > 0:
          c.b_forward()
        elif event.value < 0:
          c.b_backward()
        else:
          c.b_stop()
