#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import random
import threading


A = 10

class magorock(QtGui.QWidget):
    def __init__(self):
        super(magorock, self).__init__()
        self.setup()

    def setup(self):
        self.num = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.action)
#        self.timer.start()

        s_button = QtGui.QPushButton("Start")
#        s_button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        s_button.clicked.connect(self.start)

        t_button = QtGui.QPushButton("Stop")
#        t_button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        t_button.clicked.connect(self.stop)

        self.num = 0

        h_l = QtGui.QVBoxLayout()
        layout = QtGui.QHBoxLayout()
        layout.addWidget(s_button)
        layout.addWidget(t_button)

        h_l.addLayout(layout)

        self.setLayout(h_l)
        self.setGeometry(300,300,300,300)
        self.show()

    def action(self):
#        print self.num
        global A
        self.num = A
        self.update()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self,event,qp):
        qp.setPen(QtGui.QColor(0,0,0))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignTop,str(self.num))

class Mago_Input(threading.Thread):

    def __init__(self):
        super(Mago_Input, self).__init__()

    def run(self):
        global A
        print 'start thread'
        while True:
            A = raw_input()
            print A
            if A == '0':
                break
        print "end thread"

def main():
    magothread = Mago_Input()
    magothread.start()

    app = QtGui.QApplication(sys.argv)
    mago = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
