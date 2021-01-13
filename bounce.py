from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from pyglphys import particle2d as p2d

import datetime
from random import randint

# Global variables
delta = 0

spr = p2d.particle2d(100, 100, 8)


def buttons(key, x, y):
    pass

def display():
    global delta
    starttime = datetime.datetime.now()
    # Frame drawing calculations go here

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Object draw calls go here
    spr.draw()
    delta = ((datetime.datetime.now() - starttime).microseconds) >> 10
    glutSwapBuffers()



def phys():
    global delta
    st = datetime.datetime.now()
    # Physics calculations go here

    if(spr.y > 480):
        spr.vy *= -1
    if(spr.x > 480):
        spr.vx *= -1
    if(spr.x < 20):
        spr.vx *= -1

    delta += (datetime.datetime.now() - st).microseconds >> 10
    delta += 1 # This right here, is essential to smooth operation. It makes sure thet delta doesnt become zore, making the experience smoother overall
    # Object update calls go here. Do not do any calculations here.
    spr.update(delta)

    glutPostRedisplay()

def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0, 500, 500, 0)
    spr.ay = 0.001
    spr.vx = 0.1


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow("bounce")
init()
glutDisplayFunc(display)
glutIdleFunc(phys)
glutKeyboardFunc(buttons)
glutMainLoop()