#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QMainWindow):
    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('C:\mago.png'), 'Exiting',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.toolbar = self.addToolBar('Mago exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('toolbar')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
