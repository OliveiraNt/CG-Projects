from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi, sqrt
import sys

ESCAPE = '\033'
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
bl = 1

def tetrahedron(r):
	n = 3
	teta = 0
	x = r
	y, z = 0, 0
	a = r**2 + r**2 -2 * r * r * cos(2*pi/n)
	h = sqrt(a) * sqrt(6) / 3

	glBegin(GL_TRIANGLE_FAN)

	glColor3fv(colors[0])
	glVertex3f(0, h, 0)

	for v in range(n+1):
		glColor3fv(colors[v%8])
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()

	glBegin(GL_POLYGON)
	teta = 0
	for v in range(n+1):
		glColor3fv(colors[v%8])
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()

	#Linhas
	glBegin(GL_LINE_LOOP)
	teta = 0
	for v in range(n+1):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()

	glBegin(GL_LINES)

	glColor3fv(colors[0])

	for v in range(n+1):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(0, h, 0)
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()
	

def cube(n, r):
	teta = 0
	x = r
	y, z = 0, 0
	z2 = 2*r/sqrt(2)

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

	#linhas
	glBegin(GL_LINE_LOOP)

	teta = 0
	for v in range(n):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z2, y2)
		teta += (2*pi)/n
	glEnd()

	glBegin(GL_LINE_LOOP)

	teta = 0
	for v in range(n):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()

	for v in range(n):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glBegin(GL_LINES)
		glVertex3f(x2, z, y2)
		glVertex3f(x2, z2, y2)
		glEnd()
		teta += (2*pi)/n
	

def abacaxi():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glRotatef(2,1,3,0)
	if bl == 1 : tetrahedron(2)
	if bl == 2 : cube(4, 2)
	glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def keyPressed(*args):
	global bl

	if args[0] == ESCAPE:
		glutLeaveMainLoop()
	
	if args[0] == '1': bl = 1
	if args[0] == '2': bl = 2


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("BL")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutKeyboardFunc(keyPressed)
glutMainLoop()

