from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from  math import sin, cos, pi
import sys
from Cube import Cube
import numpy as np

cores = ( (1,1,0),(1,1,1),(0,0,1),(1.0,0.5,0.0),(0,1,0),(1,0,0))
def rc():

    matrix = np.array([
                      
                       (-1.1,+1.1,+1.1),(+0.0,+1.1,+1.1),(+1.1,+1.1,+1.1),     #(0,0,0),(0,0,1),(0,0,2)
                       (-1.1,+0.0,+1.1),(+0.0,+0.0,+1.1),(+1.1,+0.0,+1.1),     #(0,1,0),(0,1,1),(0,1,2)
                       (-1.1,-1.1,+1.1),(+0.0,-1.1,+1.1),(+1.1,-1.1,+1.1),     #(0,2,0),(0,2,1),(0,2,2)
                      
                       (-1.1,+1.1,+0.0),(+0.0,+1.1,+0.0),(+1.1,+1.1,+0.0),     #(1,0,0),(1,0,1),(1,0,2)
                       (-1.1,+0.0,+0.0),(+0.0,+0.0,+0.0),(+1.1,+0.0,+0.0),     #(1,1,0),(1,1,1),(1,1,2)
                       (-1.1,-1.1,+0.0),(+0.0,-1.1,+0.0),(+1.1,-1.1,+0.0),     #(1,2,0),(1,2,1),(1,2,2)
                      
                       (-1.1,+1.1,-1.1),(+0.0,+1.1,-1.1),(+1.1,+1.1,-1.1),     #(2,0,0),(2,0,1),(2,0,2)
                       (-1.1,+0.0,-1.1),(+0.0,+0.0,-1.1),(+1.1,+0.0,-1.1),     #(2,1,0),(2,1,1),(2,1,2)
                       (-1.1,-1.1,-1.1),(+0.0,-1.1,-1.1),(+1.1,-1.1,-1.1)      #(2,2,0),(2,2,1),(2,2,2)
                                                                          
                                                                         ])
    	
    for vect in matrix:
        c = Cube(vect,1)
        faces = c.faces
        vertices = c.vertex
        glBegin(GL_QUADS)
        i = 0
	
        for face in faces:
            glColor3fv(cores[i])
            i += 1
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()



def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    rc()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("rubik's cube")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()




