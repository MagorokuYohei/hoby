#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):

        okButton = QtGui.QPushButton("OK!!")
        cancelButton = QtGui.QPushButton("Cancel!!")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Buttons")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
