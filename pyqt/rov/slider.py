# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this example, we create a custom widget.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topright)
        splitter1.addWidget(topleft)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleamlooks'))


        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Qtgui Qsplitter')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = magorock()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
