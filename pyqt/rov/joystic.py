# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from PyQt4 import QtCore,QtGui
import sys

pygame.joystick.init()
try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print 'JoyStick_Name :' + j.get_name()
    print 'Number of Button : ' + str(j.get_numbuttons())
except pygame.error:
    print 'Please connect Joystick'

class magorock(QtGui.QWidget):

    def text_change(self, change):
        self.value = change

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def update(self):
        super(magorock,self).update()
        self.show()

    def initUI(self):
        value = QtGui.QLabel('HELLO')
#        value = QtGui.QLabel(text)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(value)

        self.setLayout(hbox)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Qtgui Qsplitter')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    mag = magorock()
#    sys.exit(app.exec_())
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
                mag.value = "nek
            elif e.type == pygame.locals.JOYBUTTONUP:
                print str(e.button)+' Button Released'

if __name__ == '__main__':
    main()
