# import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy
import time
import random
from PIL import Image

tecla = 0  # vai armazenar a tecla que for pressionada
i, j = 0.0, 0.0  # contadores
tex = None
stop_min = 540
stop_max = 2700
a = random.randrange(1, 10, 1)  # Valor random para ser usado em X no rotate
b = random.randrange(1, 10, 1)  # Valor random para ser usado em y no rotate
c = random.randrange(1, 10, 1)  # Valor random para ser usado em z no rotate
stop = random.randrange(
    stop_min, stop_max, 90
)  # valor random que irá decidir o momento do dado parar de rodar

#
def line():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-100.0, -100.0)
    glVertex2f(100.0, 100.0)
    glEnd()


def textura(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textureID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGB,
        img.size[0],
        img.size[1],
        0,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        img_data,
    )
    return textureID


def eixoXY():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-300, 0)
    glVertex2f(300, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -300)
    glVertex2f(0, 300)
    glEnd()


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300.0, 300, -300.0, 300, -300.0, 300.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def cube():
    glBegin(GL_QUADS)

    # CIMA 5
    glTexCoord2f(0.6, 0.50)
    glVertex3f(100.0, 100.0, -100.0)
    glTexCoord2f(0.4, 0.50)
    glVertex3f(-100.0, 100.0, -100.0)
    glTexCoord2f(0.4, 0.75)
    glVertex3f(-100.0, 100.0, 100.0)
    glTexCoord2f(0.6, 0.75)
    glVertex3f(100.0, 100.0, 100.0)

    # BAIXO 2
    glTexCoord2f(0.6, 0.38)
    glVertex3f(100.0, -100.0, 100.0)
    glTexCoord2f(0.4, 0.38)
    glVertex3f(-100.0, -100.0, 100.0)
    glTexCoord2f(0.4, 0.14)
    glVertex3f(-100.0, -100.0, -100.0)
    glTexCoord2f(0.6, 0.14)
    glVertex3f(100.0, -100.0, -100.0)

    # Frente 1
    glTexCoord2f(0.29, 0.38)
    glVertex3f(100.0, 100.0, 100.0)
    glTexCoord2f(0.09, 0.38)
    glVertex3f(-100.0, 100.0, 100.0)
    glTexCoord2f(0.09, 0.14)
    glVertex3f(-100.0, -100.0, 100.0)
    glTexCoord2f(0.29, 0.14)
    glVertex3f(100.0, -100.0, 100.0)

    # Trás 4
    glTexCoord2f(0.09, 0.75)
    glVertex3f(-100.0, 100.0, -100.0)
    glTexCoord2f(0.29, 0.75)
    glVertex3f(100.0, 100.0, -100.0)
    glTexCoord2f(0.29, 0.50)
    glVertex3f(100.0, -100.0, -100.0)
    glTexCoord2f(0.09, 0.50)
    glVertex3f(-100.0, -100.0, -100.0)

    # face 3
    glTexCoord2f(0.9, 0.38)
    glVertex3f(100.0, 100.0, -100.0)
    glTexCoord2f(0.71, 0.38)
    glVertex3f(100.0, 100.0, 100.0)
    glTexCoord2f(0.71, 0.14)
    glVertex3f(100.0, -100.0, 100.0)
    glTexCoord2f(0.9, 0.14)
    glVertex3f(100.0, -100.0, -100.0)

    # face 6
    glTexCoord2f(0.91, 0.51)
    glVertex3f(-100.0, 100.0, 100.0)
    glTexCoord2f(0.71, 0.51)
    glVertex3f(-100.0, 100.0, -100.0)
    glTexCoord2f(0.71, 0.75)
    glVertex3f(-100.0, -100.0, -100.0)
    glTexCoord2f(0.91, 0.75)
    glVertex3f(-100.0, -100.0, 100.0)
    glEnd()


def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result


def teclado(key, x, y):
    global tecla, a, b, c, stop, stop_min, stop_max, j
    if key == ' ':
        return None

    tecla = bytes_to_int(key)
    if tecla == 32:
        j = 0.0
        a = random.randrange(1, 10, 1)
        b = random.randrange(1, 10, 1)
        c = random.randrange(1, 10, 1)
        stop = random.randrange(stop_min, stop_max, 45)

    elif tecla == 70 or tecla == 102:
        if stop_max < 5400:
            stop_min += 720
            stop_max += 720

    elif tecla == 82 or tecla == 115:
        if stop_min > 1260:
            stop_min -= 720
            stop_max -= 720
    return None


def light():
    """Setup light 0 and enable lighting"""
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.8, 0.8, 0.8, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(2.1, 2.1, 2.1, 0.8))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 0.5, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1000, 1000, 3000, 0))
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.8, 0.8, 0.8, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def depth():
    """Setup depth testing"""
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)


def showScreen():
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    # light()
    # depth()

    glShadeModel(GL_FLAT)
    glFrontFace(GL_CCW)
    glEnable(GL_CULL_FACE)

    global tecla, a, b, c, stop
    global i, j
    global tex

    if j < stop:
        i += 1
        j += 1
    glRotated(i, a, b, c)
    light()
    depth()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)
    time.sleep(1 / (stop - j + 1))
    gluLookAt(
        0,
        1,
        20,  # eyepoint
        0,
        0,
        0,  # center-of-view
        0,
        1,
        0,  # up-vector
    )

    cube()

    glutSwapBuffers()


def main():
    global tex
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(-300, -300)
    glutCreateWindow("CUBO CUBO CUBO")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutKeyboardFunc(teclado)
    tex = textura("diago.jpeg")
    glutMainLoop()


if __name__ == "__main__":
    main()
