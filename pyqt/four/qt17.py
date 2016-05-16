#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class magorock(QtGui.QMainWindow):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30,50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'was prressed')

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
