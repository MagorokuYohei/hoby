#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):

        lbl1 = QtGui.QLabel('MAGOROCK', self)
        lbl1.move(15,10)

        lbl2 = QtGui.QLabel('is', self)
        lbl2.move(35,40)

        lbl3 = QtGui.QLabel('yellow monkey', self)
        lbl3.move(55,70)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('absolute')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
