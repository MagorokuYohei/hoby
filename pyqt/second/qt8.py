#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QMainWindow):

    def __init__(self):
        super(magorock, self).__init__()

        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Menubar')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
