# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QMainWindow):

    def __init__(self):
        super(magorock, self).__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('statusBar')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
