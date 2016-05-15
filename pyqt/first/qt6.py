#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()

        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
