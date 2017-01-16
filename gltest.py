import sys
import math
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QPoint, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QOpenGLWidget, QSlider, QWidget)
from PyQt5.Qt import QVector3D, QVector2D
from PyQt5.Qt import QTextStream
from PyQt5.Qt import QImage
from PyQt5.Qt import QFile, QIODevice, QFileInfo

# helcper class for facing represenitng the stuf from .obj file
class Face():
    def __init__(self):
        self.v = QVector3D()
        self.vn = QVector3D()
        self.f = QVector2D()


class Model():
    def __init__(self, fname):
        self.fname = fname
        self.textureName = None
        self.Vertices = list()
        self.VNormals = list()
        self.UVs = list()
        self.faces = list()

    def render(self):
        pass

    def face(self):
        pass

    def points(self):
        pass

    def __LoadMTL(self, fn, mtlName):
        pass

    def __LoadTexture(self):
        pass


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.glWidget = GLWidget()
        self.xSlider = self.createSlider()
        self.ySlider = self.createSlider()
        self.zSlider = self.createSlider()

        self.xSlider.valueChanged.connect(self.glWidget.setXRotation)
        self.glWidget.xRotationChanged.connect(self.xSlider.setValue)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.glWidget)
        self.layout.addWidget(self.xSlider)
        self.layout.addWidget(self.ySlider)
        self.layout.addWidget(self.zSlider)
        self.setLayout(self.layout)

        self.setWindowTitle("GL Widget")


    def createSlider(self):
        slider = QSlider(Qt.Vertical)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)

        return slider


class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.lastPosition = QPoint()
        self.trollTechGreen = QColor.fromCmyk(0.40, 0.0, 1.0, 0.0)
        self.trollTechPurple = QColor.fromCmyk(0.39, 0.39, 0.0, 0.0)

    def initializeGL(self):
        self.gl = self.context().versionFunctions()
        self.gl.initialzieOpenGLFunctions()
        self.setClearColor(self.trollTechPurple.darker())


    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return  angle

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if (angle != self.xRot):
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()


def main(args=()):
    app = QApplication(args)
    m = Model(args[1])
    w = Widget()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)


