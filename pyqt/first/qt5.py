#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,250)
        self.setWindowTitle('MessageBox')
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
