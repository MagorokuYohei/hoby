# -*- coding: utf-8 -*-

import sys
import random
from PyQt4 import QtCore, QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock, self).__init__()
        self.initUI()

    def initUI(self):
        self.text = 'HELLO MAGOROCK'

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        self.drawPoints(qp)
        qp.end()
    def drawText(self,event,qp):
        qp.setPen(QtGui.QColor(168,34,3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter,self.text)
    def drawPoints(self,qp):
        qp.setPen(QtCore.Qt.green)
        size = self.size()
        qp.drawRect(80,140,140,20)
        qp.setPen(QtCore.Qt.blue)

        for i in range(1000):
            x = random.randint(1,size.width()-1)
            y = random.randint(1,size.height()-1)
            qp.drawPoint(x,y)

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        color = QtGui.QColor(255,255,255)
#        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)


def main():

    app = QtGui.QApplication([])
    ex = magorock()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
