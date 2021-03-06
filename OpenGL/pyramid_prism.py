from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi
import sys

ESCAPE = '\033'
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
n = 3
bl = True

def pyramid(n, r):
	teta = 0
	x = r
	y, z = 0, 0

	glBegin(GL_TRIANGLE_FAN)

	glColor3fv(colors[0])
	glVertex3f(0, r, 0)

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
	glVertex3f(0, r, 0)

	for v in range(n+1):
		glColor3f(0,0,0)
		x2 = (x * cos(teta) - y * sin(teta))
		y2 = (x * sin(teta) + y * cos(teta))
		glVertex3f(0, r, 0)
		glVertex3f(x2, z, y2)
		teta += (2*pi)/n
	glEnd()
	

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
	if bl : pyramid(n, 2)
	else: prism(n, 2, 2)
	glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def keyPressed(*args):
	global n
	global bl

	if args[0] == ESCAPE:
		glutLeaveMainLoop()

	if args[0] == '3': n = 3
	if args[0] == '4': n = 4
	if args[0] == '5': n = 5
	if args[0] == '6': n = 6
	if args[0] == '7': n = 7
	if args[0] == '8': n = 8
	if args[0] == '9': n = 9
	
	if args[0] == ' ': 
		if bl : bl = False
		else : bl = True


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

