# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):

    closeApp = QtCore.pyqtSignal()

class magorock(QtGui.QMainWindow):
    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()