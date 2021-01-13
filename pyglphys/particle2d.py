from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class particle2d:

    def __init__(self, xpos, ypos, psize):
        """
        Instances a particle2d object, with position and size parameters
        """

        self.x = xpos
        self.y = ypos
        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0

        self.size = psize
    
    def draw(self):
        """
        Draws the particle onto the active opengl context, as a point
        """
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glVertex(self.x, self.y)
        glEnd()

    def update(self, elapsedTime):
        """
        Updates particle xpos and ypos based on velocity, acceleration and Elapsed time
        """ 
        self.x += self.vx*elapsedTime
        self.y += self.vy*elapsedTime

        self.vx += self.ax*elapsedTime
        self.vy += self.ay*elapsedTime
    