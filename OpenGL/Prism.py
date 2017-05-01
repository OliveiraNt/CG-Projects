from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from  math import sin, cos, pi
import sys


colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def prism(n, r, l):
	teta = 0
	x = r
	y, z = 0, 0
	z2 = l

	glBegin(GL_QUAD_STRIP)

	for v in range(n+1):
		glColor3fv(colors[v%8])
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		glVertex3f(x2, z2, y2)
		teta += (2*pi)/n
	glEnd()

	glBegin(GL_POLYGON)

	teta = 0
	for v in range(n):
		glColor3fv(colors[v%8])
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()

	glBegin(GL_POLYGON)

	teta = 0
	for v in range(n):
		glColor3fv(colors[v%8])
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z2, y2)
		teta += (2*pi)/n
	glEnd()
	

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    prism(3, 2, 3)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PYRAMID")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
