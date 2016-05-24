#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

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
        s_button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        s_button.clicked.connect(self.start)

        t_button = QtGui.QPushButton("Stop")
        t_button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        t_button.clicked.connect(self.stop)

        self.text = QtGui.QLabel(str(self.num))

        h_l = QtGui.QVBoxLayout()
        layout = QtGui.QHBoxLayout()
        layout.addWidget(s_button)
        layout.addWidget(t_button)
        h_l.addWidget(self.text)
        h_l.addLayout(layout)

        self.setLayout(h_l)
        self.setGeometry(300,300,300,300)
        self.show()

    def action(self):
        print self.num
        self.num += 1
        self.text.update()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    app = QtGui.QApplication(sys.argv)
    mago = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
