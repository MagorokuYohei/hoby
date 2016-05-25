#-*- coding:utf-8-*-

import sys
from PyQt4 import QtCore,QtGui
import pygame
from pygame.locals import *
import threading
import time
import socket
from contextlib import closing

b = 0
u = 0
y = 0

e = False

class mago_joy(threading.Thread):

    def __init__(self):
        super(mago_joy, self).__init__()

    def run(self):
        global b
        global u
        global y

        _j1 = 0
        _j2 = 0
        _j3 = 0

        host = '127.0.0.1'
        port = 4000
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


        pygame.joystick.init()
        try:
            j = pygame.joystick.Joystick(0)
            j.init()
            print 'Joystick name :' + j.get_name()
        except pygame.error:
            print "Please connect Joystick"
        judge = True
        pygame.init()

        up = 15

        thr_1=0.
        thr_2=0.
        thr_3=0.
        _thr_1=0.
        _thr_2=0.
        _thr_3=0.

        while judge:
            for en in pygame.event.get():
                if en.type == pygame.locals.JOYBUTTONDOWN:
                    B = []
                    for i in range(0,8):
                        B.append(j.get_button(i))
                    if B[0] == 1:# and B[1] == 1 and B[6] == 1 and B[7] == 1:
                        global e
                        e = True
                        judge = False
            time.sleep(0.05)

            j1 ,j3, j2= j.get_axis(1),j.get_axis(2),j.get_axis(3)
            j1 *=200
            j2 *=200
            j3 *=200

            if j1 - _j1 > up:
                j1 = _j1 +up
            elif j1 - _j1 <-up:
                j1 = _j1 -up
            if j1 >=0 and _j1<0:
                j1 =0
            if j1 <=0 and _j1>0:
                j1 =0

            if j2 - _j2 > up:
                j2 = _j2 +up
            elif j2 - _j2 <-up:
                j2 = _j2 -up
            if j2 >=0 and _j2<0:
                j2 =0
            if j2 <=0 and _j2>0:
                j2 =0

            if j3 - _j3 > up:
                j3 = _j3 +up
            elif j3 - _j3 <-up:
                j3 = _j3 -up
            if j3 >=0 and _j3<0:
                j3 =0
            if j3 <=0 and _j3>0:
                j3 =0

            b = j1
            u = j2
            y = j3


            thr_1 = -j1*32767*0.005 + 32767
            thr_2 = j2*32767*0.005 + 32767
            thr_3 = -j3*32767*0.005 + 32767

            if thr_1 == 32767 and _thr_1 != 32767:
                message = "S-"+str(int(thr_1))+"H-"+ str(int(thr_2))+"Y-"+str(int(thr_3))
                sock.sendto(message, (host, port))
                time.sleep(0.3)
            if thr_2 == 32767 and _thr_2 != 32767:
                message = "S-"+str(int(thr_1))+"H-"+ str(int(thr_2))+"Y-"+str(int(thr_3))
                sock.sendto(message, (host, port))
                time.sleep(0.3)
            if thr_3 == 32767 and _thr_3 != 32767:
                message = "S-"+str(int(thr_1))+"H-"+ str(int(thr_2))+"Y-"+str(int(thr_3))
                sock.sendto(message, (host, port))
                time.sleep(0.3)

            message = "S-"+str(int(thr_1))+"H-"+ str(int(thr_2))+"Y-"+str(int(thr_3))
            sock.sendto(message, (host, port))

            _thr_1 = thr_1
            _thr_2 = thr_2
            _thr_3 = thr_3

            _j1 = j1
            _j2 = j2
            _j3 = j3

        print 'Finish!!'


class magorock(QtGui.QWidget):
    def __init__(self):
        super(magorock,self).__init__()
        self.setup()

    def setup(self):
        self.num_1 = 0
        self.num_2 = 0
        self.num_3 = 0

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.action)
        self.timer.start()


        self.x = 800
        self.y = 500
        self.setWindowTitle('Magorock_Gui')
        self.resize(self.x,self.y)
        self.setStyleSheet("background-color:gray")
        self.show()

    def action(self):
        global b
        global u
        global y
        self.num_1 = b
        self.num_2 = u
        self.num_3 = y
        global e
        if e:
            self.close()

        self.update()

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(event,qp)
        qp.end()

    def draw(self, event, qp):

#        qp.setPen(QtGui.QColor(0,0,0))
#        qp.setFont(QtGui.QFont('Decorative', 15))
#        qp.drawText(event.rect(), QtCore.Qt.AlignTop, str(self.text))

        color = QtGui.QColor('#000000')
        qp.setBrush(QtGui.QColor('#FFFFFF'))
        qp.setPen(color)
        qp.drawRect(625,48,75,402)
        qp.drawRect(100,48,75,402)
        qp.drawRect(198,400,402,75)

        color = QtGui.QColor('#00ff00')
        qp.setPen(color)
        qp.setBrush(QtGui.QColor('#00ff00'))
        qp.drawRect(626,250,73,self.num_1)
        qp.drawRect(101,250,73,self.num_2)
        qp.drawRect(400,401,self.num_3,73)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    jthread = mago_joy()
    jthread.start()

    app = QtGui.QApplication(sys.argv)
    mago = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
