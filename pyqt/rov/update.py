#-*-coding:utf-8-*-

from PyQt4 import QtGui, QtCore
import sys

class button(QtGui.QWidget):

    def __init__(self):
        super(button, self).__init__()
        self.setup()

    def setup(self):
        self.start_button = QtGui.QPushButton('Start')
        self.stop_button = QtGui.QPushButton('Stop')
        self.reset_button = QtGui.QPushButton('Reset')
        self.end_button = QtGui.QPushButton('Bye')

        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(self.start_button, 0, 0)
        self.layout.addWidget(self.stop_button, 0, 1)
        self.layout.addWidget(self.reset_button, 1, 0)
        self.layout.addWidget(self.end_button, 1, 1)

        self.setLayout(self.layout)

class number(QtGui.QWidget):
    def __init__(self):
        super(number, self).__init__()
        self.interval = 10
        self.setup()

    def setup(self):
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.countdown)

        self.lcd_number = QtGui.QLCDNumber()
        self.lcd_number.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.lcd_number.setFrameStyle(QtGui.QFrame.NoFrame)
        self.lcd_number.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_number.setDigitCount(6)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.lcd_number)
        self.setLayout(self.layout)

        self.reset()

    def update_display(self):
        self.lcd_number.display("%6.2f" % (float(self.count) / 100))
        self.lcd_number.update()

    def countdown(self):
        self.count -= 1
        self.update_display()
        if self.count <= 0:
            self.stop()

    def stop(self):
        self.timer.stop()

    def start(self):
        if self.count > 0:
            self.timer.start()

    def reset(self):
        self.count = 18000
        self.update_display()



class window(QtGui.QWidget):

    def __init__(self):
        super(window, self).__init__()
        self.setup()

    def setup(self):
        button_widget = button()
        number_widget = number()

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(number_widget)
        vbox.addWidget(button_widget)

        button_widget.start_button.clicked.connect(number_widget.start)
        button_widget.stop_button.clicked.connect(number_widget.stop)
        button_widget.reset_button.clicked.connect(number_widget.reset)
        button_widget.end_button.clicked.connect(self.bye)

        self.setLayout(vbox)
        self.setWindowTitle('Mago Timer')
        self.setGeometry(300,300,300,300)
        self.show()

    def bye(self):
        self.close()


def main():
    app = QtGui.QApplication(sys.argv)
    mago = window()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
