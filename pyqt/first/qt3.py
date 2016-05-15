# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):
    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip("This is a <b>Qwidget</b> widget")

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,250,250)
        self.setWindowTitle("tooltips")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex  = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
