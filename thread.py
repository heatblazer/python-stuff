"""Demo of qthread using under pyqt"""

import sys
from PyQt5.QtCore import *


class MyObject(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__sig1 = pyqtSignal()
        self.__val = 10
        print("Parent got")

    def cnageVal(self, newVal):
        self.__val = newVal
        self.__sig1.emit(self.__val)
#


class ValHandler(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.constant = (10,)

    def errChange(self):
        return self.constant[0]
#


class PThread(QThread):

    def run(self):
        while self.isRunning:
            print("Running ...\n")
            QThread.usleep(100)

    def stopThread(self):
        self.isRunning = False
        self.wait(1000)


def main():
    app = QCoreApplication(sys.argv)
    myo = ValHandler()
    print(myo.errChange())
    threads = [MyObject() for i in range(10)]
"""
    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].stopThread()

    sys.exit(app.exec_())
"""


if __name__ == "__main__":
    main()

