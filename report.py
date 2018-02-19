from OpenGL.GL import *
from OpenGL.GLUT import *

def draw1():
    #background
    glBegin(GL_POLYGON)
    glColor3d(1, 1, 1)
    glVertex2d(1, 1)
    glVertex2d(1, -1)
    glVertex2d(-1, -1)
    glVertex2d(-1,1)
    glEnd()


    #body
    glBegin(GL_POLYGON)
    glColor3d(0, 0, 0)
    glVertex2d(-0.25, -0.25)
    glVertex2d( 0.25, -0.25)
    glVertex2d( 0.25, 0.25)
    glVertex2d(-0.25, 0.25)
    glEnd()


    #nick
    glBegin(GL_POLYGON)
    glColor3d(0.8, 1, 0)
    glVertex2d(-0.075, 0.25)
    glVertex2d(0.075, 0.25)
    glVertex2d(0.075, 0.35)
    glVertex2d(-0.075, 0.35)
    glEnd()


    #head
    glBegin(GL_POLYGON)
    glColor3d(0.7, 1, 0)
    glVertex2d(-0.15, 0.35)
    glVertex2d(0.15, 0.35)
    glVertex2d(0.15, 0.6)
    glVertex2d(-0.15, 0.6)
    glEnd()


    #left hand
    glBegin(GL_POLYGON)
    glColor3d(0.0, 0, 0)
    glVertex2d(-.25, 0.25)
    glVertex2d(-0.55, 0.25)
    glVertex2d(-0.55, 0.1)
    glVertex2d(-0.25, 0.1)
    glEnd()
    #right hand
    glBegin(GL_POLYGON)
    glColor3d(0.0, 0.0, 0)
    glVertex2d(.25, 0.25)
    glVertex2d(0.55, 0.25)
    glVertex2d(0.55, 0.1)
    glVertex2d(0.25, 0.1)
    glEnd()


    #left leg
    glBegin(GL_POLYGON)
    glColor3d(0.0, 0, 0)
    glVertex2d(-.25, -0.25)
    glVertex2d(-0.1, -0.25)
    glVertex2d(-0.1, -0.55)
    glVertex2d(-0.25, -0.55)
    glEnd()
    #right leg
    glBegin(GL_POLYGON)
    glColor3d(0.0, 0, 0)
    glVertex2d(.25, -0.25)
    glVertex2d(0.1, -0.25)
    glVertex2d(0.1, -0.55)
    glVertex2d(0.25, -0.55)
    glEnd()


    #left rest
    glBegin(GL_POLYGON)
    glColor3d(0.8, 1, 0)
    glVertex2d(-.55,.25)
    glVertex2d(-.55, .3)
    glVertex2d(-.6, .3)
    glVertex2d(-.6, .25)
    glVertex2d(-.7, .25)
    glVertex2d(-.7, .1)
    glVertex2d(-.55, .1)
    glEnd()
    # right rest
    glBegin(GL_POLYGON)
    glColor3d(.8, 1, 0)
    glVertex2d(.55, .25)
    glVertex2d(.55, .3)
    glVertex2d(.6, .3)
    glVertex2d(.6, .25)
    glVertex2d(.7, .25)
    glVertex2d(.7, .1)
    glVertex2d(.55, .1)
    glEnd()


    #left shoe
    glBegin(GL_POLYGON)
    glColor3d(0.2, 0.2, 0.2)
    glVertex2d(-.26, -0.63)
    glVertex2d(-0.09, -0.63)
    glVertex2d(-0.09, -0.55)
    glVertex2d(-0.26, -0.55)
    glEnd()
    # right shoe
    glBegin(GL_POLYGON)
    glColor3d(0.2, 0.2, 0.2)
    glVertex2d(.26, -0.63)
    glVertex2d(0.09, -0.63)
    glVertex2d(0.09, -0.55)
    glVertex2d(0.26, -0.55)
    glEnd()


    #left eye
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(-.1, 0.55)
    glVertex2d(-0.05, 0.55)
    glVertex2d(-0.05, 0.5)
    glVertex2d(-0.1, 0.5)
    glEnd()
    #right eye
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(.1, 0.55)
    glVertex2d(0.05, 0.55)
    glVertex2d(0.05, 0.5)
    glVertex2d(0.1, 0.5)
    glEnd()


    #mouth
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(-.1, 0.45)
    glVertex2d(.1, 0.45)
    glVertex2d(0.1, 0.4)
    glVertex2d(-0.1, 0.4)
    glEnd()


    #shirt
    glBegin(GL_POLYGON)
    glColor3d(1, 1, 1)
    glVertex2d(-.05, -0.2)
    glVertex2d(0.05, -0.2)
    glVertex2d(0.05, 0.25)
    glVertex2d(-0.05, 0.25)
    glEnd()


    #caravat around the nick
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(-.05, 0.25)
    glVertex2d(0.05, 0.25)
    glVertex2d(0.05, 0.22)
    glVertex2d(-0.05, 0.22)
    glEnd()
    #caravat above the shirt
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(-.025, 0.22)
    glVertex2d(0.025, 0.22)
    glVertex2d(0.025, -0.1)
    glVertex2d(-0.025, -0.1)
    glEnd()
    #the triangle end of the caravat
    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex2d(0, -0.15)
    glVertex2d(0.025, -0.1)
    glVertex2d(-0.025, -0.1)
    glEnd()
    glFlush()
    ##---------------------------------------------------##


glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"robot") # Set the window's initial width & height
glutDisplayFunc(draw1)
glutMainLoop()