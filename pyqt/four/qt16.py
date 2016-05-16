#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('event handler')
        self.show()

    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
