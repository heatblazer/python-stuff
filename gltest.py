import sys
import ctypes
import numpy
from PyQt4 import QtGui
from PyQt4.QtOpenGL import *
from OpenGL.GL import *

"""opens a simple QtGl window and draws basick shapes..."""

class GlWidget(QGLWidget):
    def __init__(self, parent = None):
        super(GlWidget, self).__init__(parent)

    def paintGL(self):
        glColor3f(1.0, 0.0, 0.0)
        glRectf(-5, -5, 5, 5)
        glBegin(GL_LINES)
        glVertex3f(0,0,1)
        glVertex3f(20, 20, 0)
        glEnd()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        glViewport(0,0, w, h)


def main(args=()):
    app = QtGui.QApplication(args)
    glwidget = GlWidget()
    glwidget.show()
    return app.exec_()


if __name__ == '__main__':
    main([])


