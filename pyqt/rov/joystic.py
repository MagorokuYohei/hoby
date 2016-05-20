# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.joystick.init()
try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print 'JoyStick_Name :' + j.get_name()
    print 'Number of Button : ' + str(j.get_numbuttons())
except pygame.error:
    print 'Please connect Joystick'

def main():
    pygame.init()
    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if (e.type == KEYDOWN and
                e.key  == K_ESCAPE):
                return
#            print e
            if e.type == pygame.locals.JOYAXISMOTION:
                x , y ,z= j.get_axis(0), j.get_axis(1),j.get_axis(2)
                q= j.get_axis(3)
                print 'x and y and : ' + str(x) +' , '+ str(y)
                print 'left status : ' + str(z) +' , '+ str(q)
            elif e.type == pygame.locals.JOYHATMOTION:
                print 'hat motion'
                print str(e.value)
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print str(e.button)+' Button Pushed'
            elif e.type == pygame.locals.JOYBUTTONUP:
                print str(e.button)+' Button Released'

if __name__ == '__main__':
    main()
