#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name')

        if ok:
            self.le.setText(str(text))

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
