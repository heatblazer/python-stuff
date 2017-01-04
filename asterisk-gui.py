import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QSize
from PyQt4.QtCore import QByteArray
from PyQt4.QtCore import QTimer


class MyObject(QObject):
    sig1 = pyqtSignal()
    sig2 = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def addSome(self, val):
        self.sig1.emit(val)


class Console(QtGui.QPlainTextEdit):

    def __init__(self):
        super(Console, self).__init__()
        self.setReadOnly(True)
        self.setMinimumSize(320, 460)
        self.setMaximumSize(320, 460)
        p = QtGui.QPalette()
        p.setColor(QtGui.QPalette.Base, QtGui.QColor("black"))
        p.setColor(QtGui.QPalette.Text, QtGui.QColor("green"))
        self.setPalette(p)
        self.textChanged.connect(self.hTextChange)

    def putData(self, data):
        assert isinstance(data, str)
        self.insertPlainText(data)

    def hData(self):
        pass

    def hTextChange(self):
        c = QtGui.QTextCursor(self.textCursor())
        c.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.setTextCursor(c)


class Gui(QtGui.QWidget):
    """Iner class """
    class CallWidget(QtGui.QVBoxLayout):

        def __init__(self):
            super(Gui.CallWidget, self).__init__()
            self.text = QtGui.QTextEdit()
            self.text.setMinimumSize(200, 25)
            self.text.setMaximumSize(200, 25)
            self.button1 = QtGui.QPushButton()
            self.button1.setText("DIAL")
            self.button1.setMinimumSize(100, 25)
            self.button2 = QtGui.QPushButton()
            self.button2.setText("HUP")
            self.button2.setMinimumSize(100, 25)
            self.button3 = QtGui.QPushButton()
            self.button3.setText("Echo test")
            self.button3.setMinimumSize(100, 25)
            self.button3.clicked.connect(self.hButton3)
            self.addWidget(self.text)
            self.addWidget(self.button1)
            self.addWidget(self.button2)
            self.addWidget(self.button3)

        def hButton3(self):
            print("Clicked b3")

    def __init__(self):
        super(Gui, self).__init__()

        self.m_hbox = QtGui.QHBoxLayout()
        self.m_leftVbox = QtGui.QVBoxLayout()
        self.m_rightVbox = QtGui.QVBoxLayout()
        self.m_midVbox = QtGui.QVBoxLayout()

        self.m_callW = Gui.CallWidget()
        self.m_midVbox.addLayout(self.m_callW)
        self.m_console = Console()

        self.m_leftVbox.addWidget(self.m_console)

        self.m_hbox.addLayout(self.m_leftVbox)
        self.m_hbox.addLayout(self.m_midVbox)

        self.setMinimumSize(QSize(1024, 480))
        self.setMaximumSize(QSize(1024, 480))
        self.setLayout(self.m_hbox)
        #delete after tests ...
        self.m_console.show()

        self.m_timer = QTimer()
        self.m_timer.setInterval(1000)
        self.m_timer.timeout.connect(self.hTimeout)
        self.m_timer.start()

    def hTimeout(self):
        self.m_console.putData(str("bla bla bla.. time has passed away..\n"))

    def hClick3(self):
        print("Echo test!")


def main():
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
