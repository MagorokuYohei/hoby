#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class magorock(QtGui.QWidget):

    def __init__(self):
        super(magorock,self).__init__()
        self.initUI()


    def initUI(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit= QtGui.QLineEdit()
        reviewEdit= QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1,0)
        grid.addWidget(titleEdit, 1,1)

        grid.addWidget(author, 2,0)
        grid.addWidget(authorEdit, 2,1)

        grid.addWidget(review, 3,0)
        grid.addWidget(reviewEdit, 3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Review')
        self.show()

def main():
    print "BAKEMONO"
    app = QtGui.QApplication(sys.argv)
    mago = magorock()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
