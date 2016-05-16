# -*-coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names =['Cls','Bck', '', 'Close',
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, * position)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()

def main():
    print "BAKEMONO"
    app = QtGui.QApplication(sys.argv)
    mag = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
