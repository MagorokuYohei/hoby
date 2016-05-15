# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()
