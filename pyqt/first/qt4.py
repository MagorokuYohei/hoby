# -*-coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,250)
        self.setWindowTitle('quit button')
        self.show()

    def hellow(self):
        print "HELLOW"

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
