from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

n1 = 50
n2 = 50
r = 2
a = 0

def f(i, j):
    theta = (math.pi * i / (n1 - 1)) - (math.pi / 2)
    phi = 2 * math.pi * j / (n2 - 1)
    x = (r * math.cos(theta)) * math.cos(phi)
    y = r * math.sin(theta)
    z = (r * math.cos(theta)) * math.sin(phi)
    return x, y**2, z

def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix() # Guarda o estado de transformação da matriz atual (matriz M)
    
    # glRotatef(angulo, x, y, z)
    glRotatef(a,1.0,1.0,1.0) # Fazendo matriz atual N = M * rotação
    for i in range(0, round(n1/2)): #Variação do teta
        glBegin(GL_QUAD_STRIP)
        for j in range(0, n2): # Variação do phi
            x, y, z = f(i, j)
            x1, y1, z1 = f(i + 1, j)

            red = 1
            green = 1-((i+1)/(n1-1))
            blue = 0
            glColor3fv((red, green, blue))
            glVertex3f(x, y, z)
            glVertex3f(x1, y1, z1)
        glEnd()
    glPopMatrix() # Voltando ao estado de transformação antes do glPushMatrix (voltando à matriz M)
    a+=1
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Paraboloid with revolution")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0) # Aplica matriz perspectiva ao universa
glTranslatef(0.0, -1.0, -10) # Empurrando 20 und para dentro da tela do PC
glutTimerFunc(10, timer, 1)
glutMainLoop()