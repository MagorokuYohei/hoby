import pygame
from pygame.locals import *
import socket
from contextlib import closing
import time


def main():
    host = '127.0.0.1'
    port = 4000
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    pygame.joystick.init()
    try:
        j = pygame.joystick.Joystick(0) # create a joystick instance
        j.init() # init instance
        print 'JoyStick_Name :' + j.get_name()
        print 'Number of Button : ' + str(j.get_numbuttons())
    except pygame.error:
        print 'Please connect Joystick'
    b_, u_, y_ = 0,0,0
    pygame.init()
    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if (e.type == KEYDOWN and
                e.key  == K_ESCAPE):
                return
        time.sleep(0.1)

#        for e in pygame.event.get():
        g, b ,u,y= j.get_axis(0), j.get_axis(1),j.get_axis(2),j.get_axis(3)
        b = int(b*(-32767))
        u = int(u*(-32767))
        y = int(y*(32768))

        if b<1000 and b>-1000:
            b = 0


        if (b-b_) > 500 :
            if b_ > 32000:
                b = 32500
            else:
                b = b_+2000
        elif (b-b_) < -500:
            if b_ < -32000:
                b = -32500
            else:
                b = b_-2000

        if (b>0 and b_<0) or (b<0 and b_>0):
            b = 0
            time.sleep(0.4)



        if (u-u_) > 500:
            u = u_+500
        elif (u-u_) < 500:
            u = u_-500

        if (y-y_) > 500:
            y = y_+500
        elif (y-y_) < 500:
            y = y_-500



        print 'Go or Back :'+str(b)
#        print 'UP or DOWN :'+str(u)
#        print 'Yaw :' + str(y)
        message = "S-"+str(b)#+"H-" + str(u)+"Y-"+str(y)
        sock.sendto(message, (host, port))

        b_ = b
        u_ = u
        y_ = y

        """
        if e.type == QUIT:
            return
        if (e.type == KEYDOWN and
            e.key  == K_ESCAPE):
            return
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
        """
    print "Finish!!"

if __name__=='__main__':
  main()
