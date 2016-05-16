# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vlcd= QtGui.QLCDNumber(self)
        vsld= QtGui.QSlider(QtCore.Qt.Vertical, self)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(vlcd)
        hbox.addWidget(vsld)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        hbox.addLayout(vbox)

        self.setLayout(hbox)
        sld.valueChanged.connect(lcd.display)
        vsld.valueChanged.connect(vlcd.display)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Single & slot')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
