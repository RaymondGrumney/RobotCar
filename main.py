#!/bin/python3
import pygame
from CarMove import *

XBOXONE_JOYPAD=1536
UP_DOWN=1
LEFT_RIGHT=0

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

c=CarMove()

while keepPlaying:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == XBOXONE_JOYPAD:
      if event.axis == UP_DOWN:
        c.speed=int(abs(event.value) * 99)
        if event.value < 0:
          c.forward()
#          print(abs(event.value) * 99)
 #         print( "Up " )
        else:
          c.backward()
  #        print(abs(event.value)*99)
   #       print ( "Down" )
      if event.axis == LEFT_RIGHT:
        if event.value > 0:
          c.left()
          print( "Left" )
        else:
          c.right()
          print( "Right" )

