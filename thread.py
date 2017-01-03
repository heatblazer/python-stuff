"""Demo of qthread using under pyqt"""

import sys
from PyQt5.QtCore import *


class PThread(QThread):

    def run(self):
        while self.isRunning:
            print("Running ...\n")
            QThread.usleep(100)


def main():
    app = QCoreApplication([])
    threads = [PThread() for i in range(10)]

    for i in range(10):
        threads[i].start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

