import pygame
from pygame.locals import *
import socket
from contextlib import closing
import time


def main():

    pygame.joystick.init()
    try:
        j = pygame.joystick.Joystick(0) # create a joystick instance
        j.init() # init instance
        print 'JoyStick_Name :' + j.get_name()
        print 'Number of Button : ' + str(j.get_numbuttons())
    except pygame.error:
        print 'Please connect Joystick'
    judge = True
    pygame.init()
    while judge:
        time.sleep(0.1)
        for e in pygame.event.get():
            if e.type == pygame.locals.JOYBUTTONDOWN:
                print str(e.button)+' Button Pushed'
                judge = False
            if e.type == pygame.locals.JOYAXISMOTION:
                x , y= j.get_axis(0), j.get_axis(1)
                z    = j.get_axis(2)
                print 'x and y and %.2f  %.2f: '%(x ,y)
                print 'z %.2f'%(z)
#                print 'left status : ' + str(z) +' , '+ str(q)
            elif e.type == pygame.locals.JOYHATMOTION:
                print 'hat motion'
                print str(e.value)
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print str(e.button)+' Button Pushed'
            elif e.type == pygame.locals.JOYBUTTONUP:
                print str(e.button)+' Button Released'

    print "Finish!!"

if __name__=='__main__':
  main()
