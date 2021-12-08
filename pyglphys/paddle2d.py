from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class paddle2d:

    def __init__(self, xpos, ypos, xsize, ysize):
        """
        Instances a paddle2d object, with position and size parameters
        """

        self.x = xpos
        self.y = ypos
        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0

        self.xsize = xsize
        self.ysize = ysize
    
    def draw(self):
        """
        Draws the particle onto the active opengl context, as a point
        """
        glBegin(GL_QUADS)
        xoff = self.xsize/2
        yoff = self.ysize/2
        glVertex(self.x - xoff, self.y - yoff)
        glVertex(self.x + xoff, self.y - yoff)
        glVertex(self.x + xoff, self.y + yoff)
        glVertex(self.x - xoff, self.y + yoff)
        glEnd()

    def update(self, elapsedTime):
        """
        Updates particle xpos and ypos based on velocity, acceleration and Elapsed time
        """ 
        self.x += self.vx*elapsedTime
        self.y += self.vy*elapsedTime

        self.vx += self.ax*elapsedTime
        self.vy += self.ay*elapsedTime
