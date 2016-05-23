#-*-coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, QtOpenGL

class magorock(QtGui.QWidget):
  num_x = 20
  num_y = 20
  pos_x = 0
  pos_y = 0


  def __init__(self):
    super(magorock, self).__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(300,300,900,450)
    self.setWindowTitle('Magorock Gui')
    self.show()

  def paintEvent(self, e):
    qp = QtGui.QPainter()
    qp.begin(self)
    self.drawrect(qp)
    qp.end()

  def drawrect(self,qp):
    qp.setBrush(QtGui.QColor(200,0,0))
    qp.drawRect(self.pos_x,self.pos_y,self.num_x,self.num_y)

  def keyPressEvent(self,e):
    if e.key() == QtCore.Qt.Key_B:
      self.num_x += 10
      self.num_y += 10
    if e.key() == QtCore.Qt.Key_S:
      self.num_x -= 10
      self.num_y -= 10
    if e.key() == QtCore.Qt.Key_Up:
      self.pos_y -= 10
    if e.key() == QtCore.Qt.Key_Down:
      self.pos_y += 10
    if e.key() == QtCore.Qt.Key_Right:
      self.pos_x += 10
    if e.key() == QtCore.Qt.Key_Left:
      self.pos_x -= 10
    self.update()





def main():
  app = QtGui.QApplication(sys.argv)
  mag = magorock()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()
