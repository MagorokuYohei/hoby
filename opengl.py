# -*-coding:utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("OpenGL Python")
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__=="__main__":
    main()
