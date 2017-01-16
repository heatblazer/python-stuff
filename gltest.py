import sys
import math
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QPoint, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QOpenGLWidget, QSlider, QWidget)
from PyQt5.Qt import QVector3D, QVector2D
from PyQt5.Qt import QTextStream
from PyQt5.Qt import QImage
from PyQt5.Qt import QFile, QIODevice, QFileInfo
from OpenGL.GL import *
from OpenGL import *


def MTL(filename):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if (line.startswith('#')): continue
        values = line.split()
        if not values: continue
        if values[0] == "newmtl":
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError("mtl does not start with newmtl stmt")
        elif values[0] == "map_Kd":
            mtl[values[0]] = values[1]
            surface = QImage()
            surface.load()




class OBJ():
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.textcoords = []
        self.faces = []

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == "v":
                v = map(float, values[1:4])
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == "vn":
                v = map(float, values[1:4])
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == "vt":
                self.textcoords.append(map(float, values[1:3]))
            elif values[0] in ("usemtl", "usemat"):
                material = values[1]
            elif values[0] == "mtllib":
                self.mtl = MTL(values[1])
            elif values[0] == "f":
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split("/")
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append(face, norms, texcoords, material)


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


