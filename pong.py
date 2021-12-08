from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from pyglphys import particle2d as p2d

import datetime
from random import randint


# Global variables
delta = 0

p1 = 250

pv = 0.5

spr = p2d.particle2d(100, 100, 8)

# Utility function: Signum
def sgn(val):
    """
    Returns 1, -1 or 0 based on sign of input
    """
    try:
        out = val/abs(val)
    except:
        out = 0
    return out

# Function that handles input callback
def buttons(key, x, y):
    pass

# Main display callback
def display():
    global delta
    starttime = datetime.datetime.now()
    # Frame drawing calculations go here
    # In tihs case, the particle wraps aroung the screen

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Object draw calls go here
    spr.draw()

    glutSwapBuffers()

    delta = ((datetime.datetime.now() - starttime).microseconds) >> 10

def phys():

    global delta
    st = datetime.datetime.now()
    # Physics calculations go here

    # spr.ax = -sgn(spr.vx) * friction
    # spr.ay = -sgn(spr.vy) * friction
    #
    # if(abs(spr.vx) > maxspeed):
    #     spr.vx = sgn(spr.vx)*maxspeed
    # if(abs(spr.vy) > maxspeed):
    #     spr.vy = sgn(spr.vy)*maxspeed

    if(spr.x > 480):
        spr.vx *= -1
    if(spr.x < 20):
        spr.vx *= -1
    if(spr.y > 480):
        spr.vy *= -1
    if(spr.y < 20):
        spr.vy *= -1

    delta += (datetime.datetime.now() - st).microseconds >> 10
    delta += 1 # This right here, is essential to smooth operation. It makes sure thet delta doesnt become zore, making the experience smoother overall
    # Object update calls go here. Do not do any calculations here.
    spr.update(delta)

    glutPostRedisplay()




def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0, 500, 500, 0)
    spr.vx = 0.1
    spr.vy = 0.4


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow("movingpoint")
init()
glutDisplayFunc(display)
glutIdleFunc(phys)
glutKeyboardFunc(buttons)
glutMainLoop()
