from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from backend import *

window_width = 800
window_height = 600

def loadImage(imageName):
	im = Image.open(imageName)
	try:
	    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGB", 0, -1)
	except SystemError:
	    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGB", 0, -1)
	glEnable(GL_TEXTURE_2D)
	ID = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, ID)

	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

	glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
	return ID

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(1.0, 1.0, 1.0, 1.0) # White color for background
	#glClearColor(0.3, 0.3, 0.3, 1.0) # Gray Color for background
	glMatrixMode(GL_PROJECTION) # Выбираем матрицу проекций
	glLoadIdentity()            # Сбрасываем все предыдущие трансформации
	gluPerspective(90, window_width / window_height, 0.001, 10) # Задаем перспективу
	#gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Define draw edges for horisontal and vertical
	global anglex, angley, anglez, zoom, filled, texID, height_map, camPOS, camDIR, camUP
	anglex = 0
	angley = 0
	anglez = 0
	zoom   = 1.0
	filled = 1
	camPOS = Vector3(0,0,0)
	camDIR = Vector3(0,1,1)
	camUP = Vector3(0,0,1)
	texID = loadImage("skybox.png")

def texCube():
	glBegin(GL_QUADS)
	glTexCoord2f(0.75, 0.0); glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(0.5, 0.0); glVertex3f( 1.0, -1.0,  1.0)
	glTexCoord2f(0.5, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.75,0.5); glVertex3f(-1.0,  1.0,  1.0)
	
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.0, 0.5); glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)
	glTexCoord2f(0.25, 0.0); glVertex3f( 1.0, -1.0, -1.0)
	
	glTexCoord2f(0.25, 1.0); glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.5, 1.0); glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(0.5, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)
	
	glTexCoord2f(0.5, 0.5); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.5, 1.0); glVertex3f( 1.0, -1.0, -1.0)
	glTexCoord2f(0.75, 1.0); glVertex3f( 1.0, -1.0,  1.0)
	glTexCoord2f(0.75, 0.5); glVertex3f(-1.0, -1.0,  1.0)
	
	glTexCoord2f(0.25, 0.0); glVertex3f( 1.0, -1.0, -1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)
	glTexCoord2f(0.5, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.5, 0.0); glVertex3f( 1.0, -1.0,  1.0)
	
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.75, 0.0); glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(0.75, 0.5); glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(1.0, 0.5); glVertex3f(-1.0,  1.0, -1.0)
	
	glEnd()

# Processing usual keys
def keyboardkeys(key, x, y):
	global anglex, angley, anglez, zoom, filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b'w':
		anglex += 5
	if key == b's':
		anglex -= 5
	if key == b'q':
		angley += 5
	if key == b'e':
		angley -= 5
	if key == b'a':
		anglez += 5
	if key == b'd':
		anglez -= 5
	if key == b'-':
		zoom /= 1.1
	if key == b'=':
		zoom *= 1.1
	if key == b' ':
		filled = 1 - filled
	"""
	if key == b'u':
		camPOS = camPOS.plusV(camDIR.xR(0.05))
	if key == b'j':
		camPOS = camPOS.minusV(camDIR.xR(0.05))
	if key == b'k':
                rotM = Matrix3x3.MRot(camUP, 3.14/18)
                camDIR = rotM.xV(camDIR)
	if key == b'h':
                rotM = Matrix3x3.MRot(camUP, -3.14/18)
                camDIR = rotM.xV(camDIR)
	if key == b'i':
                rotM = Matrix3x3.MRot(camUP, 3.14/18)
                camUP = rotM.xV(camDIR)
	if key == b'y':
                rotM = Matrix3x3.MRot(camUP, -3.14/18)
                camUP = rotM.xV(camDIR)
	if key == b'o':
                vect = camDIR.xV(camUP)
                rotM = Matrix3x3.MRot(vect, 3.14/18)
                camUP = rotM.xV(camUP)
                camDIR = rotM.xV(camDIR)
	if key == b'l':
                vect = camDIR.xV(camUP)
                rotM = Matrix3x3.MRot(vect, -3.14/18)
                camUP = rotM.xV(camUP)
                camDIR = rotM.xV(camDIR)
        """
	glutPostRedisplay()         # Call Redraw

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear Window and Depth buffer
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	global anglex, angley, anglez, zoom, filled, texID, camPOS, camDIR, camUP, height_map
	filled = 1
	gluLookAt(camPOS.x, camPOS.y, camPOS.z,
                  camPOS.x+camDIR.x,camPOS.y+camDIR.y, camPOS.z+camPOS.z,
                  camUP.x,camUP.y,camUP.z)
	glRotated(anglex,1,0,0)
	glRotated(angley,0,1,0)
	glRotated(anglez,0,0,-1)
	glScaled(zoom, zoom, zoom)
	if filled == 1:
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	else:
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

	glColor3f(3, 1, 1)
	glScaled(zoom,zoom,zoom)
	glBindTexture(GL_TEXTURE_2D, texID)
	texCube()

	glutSwapBuffers()           # Swap Buffers
	glutPostRedisplay()         # Redraw Window

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
glutDisplayFunc(draw) # Bind function for drawing
glutKeyboardFunc(keyboardkeys) # Bind function for processing usual keys
init() # Call our Initialisation function
glutMainLoop()
