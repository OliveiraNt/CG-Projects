from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def pyramid(n, r):
	PI = 3.1415926535897932384626433832795
	teta = 0
	x = r
	y, z = 0, 0
	c = 0

	glBegin(GL_TRIANGLE_FAN)

	glColor3fv(colors[c])
	glVertex3f(0, r, 0)

	for v in range(n+1):
		glColor3fv(colors[c])
		x2 = (x * math.cos(teta) - y * math.sin(teta))
		y2 = (x * math.sin(teta) + y * math.cos(teta))
		glVertex3f(x2, z, y2)
		teta += (360/n)*PI/180
		c += 1
	glEnd()
	

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    pyramid(6, 2)
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


