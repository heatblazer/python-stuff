import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class MyWidget(QtGui.QWidget):
    """some privacty emulation..."""
    class Private():
        def __init__(self):
            self.slot_foo = self.__slot_foo

        def __slot_foo(self):
            print("Clicked!\n")

    def __init__(self):
        super(MyWidget, self).__init__()
        self.privates = self.Private()
        self.layout = QtGui.QVBoxLayout()
        self.buttons = [QtGui.QPushButton() for i in range(5)]
        self.setupUI()

    def setupUI(self):
        """private method"""
        for i in range(5):
            self.buttons[i].setMinimumSize(50, 50)
            self.buttons[i].setText(str("Button"+str(i)))
            self.buttons[i].clicked.connect(self.privates.slot_foo)
            self.layout.addWidget(self.buttons[i])

        self.setLayout(self.layout)


def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWidget()
    w.show()
    p = w.Private()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

