import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime

tmpSeconds=0
currentTime=0

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.setWindowTitle('devEffort by 10000h by self')
        self.setGeometry(100, 100, 600, 280)
        r = open(os.path.abspath('Desktop/devEffort/devEffort.ini'), mode='rt', encoding='utf-8')
        global currentTime
        currentTime = r.read()

        layout = QVBoxLayout()

        self.lcd = QLCDNumber()
        self.lcd.display('')
        self.lcd.setDigitCount(8)
        subLayout = QHBoxLayout()

        self.btnStart = QPushButton("시작")
        self.btnStart.clicked.connect(self.onStartButtonClicked)

        self.btnStop = QPushButton("멈춤")
        self.btnStop.clicked.connect(self.onStopButtonClicked)

        layout.addWidget(self.lcd)

        subLayout.addWidget(self.btnStart)
        subLayout.addWidget(self.btnStop)
        layout.addLayout(subLayout)

        self.btnStop.setEnabled(False)
        self.setLayout(layout)

    def onStartButtonClicked(self):     # read time num by devEffort.ini
        self.timer.start()
        self.btnStop.setEnabled(True)
        self.btnStart.setEnabled(False)

    def onStopButtonClicked(self):      # devEffort.ini에 - save currentTime
        self.timer.stop()
        f = open(os.path.abspath('Desktop/devEffort/devEffort.ini'), mode='wt', encoding='utf-8')
        f.write(str(tmpTime))
        self.btnStop.setEnabled(False)
        self.btnStart.setEnabled(True)

    def timeout(self):
        global tmpSeconds
        tmpSeconds+=1
        sender = self.sender()
        global tmpTime
        tmpTime= int(currentTime) - tmpSeconds
        if id(sender) == id(self.timer):
            self.lcd.display("{}".format(tmpTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())