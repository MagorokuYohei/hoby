#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui


class magorock(QtGui.QMainWindow):

  def __init__(self):
    super(magorock, self).__init__()
    self.initUI()

  def initUI(self):
    textEdit = QtGui.QTextEdit()
    self.setCentralWidget(textEdit)

    exitAction = QtGui.QAction(QtGui.QIcon('C:\mago.png'), 'Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(self.close)

    self.statusBar()

    menubar = self.menuBar()
    filemenu= menubar.addMenu('&File')
    filemenu.addAction(exitAction)

    toolbar = self.addToolBar('Exit')
    toolbar.addAction(exitAction)

    self.setGeometry(300,300,300,300)
    self.setWindowTitle('Main window')
    self.show()


def main():
  app = QtGui.QApplication(sys.argv)
  mag = magorock()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()
