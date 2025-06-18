import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# Global variables
y = 0
ang = 0
i = 0
k = 0
n = 0
a, b, c, d = 900, 880, 900, 900
p, q, s = 0, 0, 0
g = 0  # car translate indicator
m, j, o = 0.80, 0.50, 0.15


def sea():
    glColor3f(0.0, 0.50, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)
    glVertex2f(2000.0, 0.0)
    glVertex2f(2000.0, 1600.0)
    glVertex2f(0.0, 1600.0)
    glEnd()

    glPushMatrix()
    glTranslatef(0, q, 0)

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for p in range(0, 20000, 100):
        for s in range(0, 20000, 100):
            glVertex2f(100.0 + s, 100.0 + p)
            glVertex2f(200.0 + s, 100.0 + p)
    glEnd()

    glPopMatrix()


def bridge():
    global k, n
    glColor3f(0.40, 0.40, 0.40)
    glBegin(GL_QUADS)
    glVertex2f(0.0, 900.0)
    glVertex2f(500.0, 900.0)
    glVertex2f(500.0, 1200.0)
    glVertex2f(0.0, 1200.0)
    glEnd()

    # Draw the moving part of the bridge
    glPushMatrix()
    glColor3f(0.46, 0.46, 0.46)
    glBegin(GL_QUADS)
    glVertex2f(500.0, 900.0)
    glVertex2f(900.0 - k, 900.0 + n)
    glVertex2f(900.0 - k, 1200.0 + n)
    glVertex2f(500.0, 1200.0)
    glEnd()
    glPopMatrix()

    # Draw the right side of the bridge
    glColor3f(0.40, 0.40, 0.40)
    glBegin(GL_QUADS)
    glVertex2f(1300.0, 900.0)
    glVertex2f(2000.0, 900.0)
    glVertex2f(2000.0, 1200.0)
    glVertex2f(1300.0, 1200.0)
    glEnd()


def boat():
    global y, m, j, o
    glPushMatrix()
    glTranslatef(0, y, 0)

    glColor3f(m, j, o)
    glBegin(GL_POLYGON)
    glVertex2f(900.0, 700.0)
    glVertex2f(800.0, 620.0)
    glVertex2f(750.0, 500.0)
    glVertex2f(750.0, 200.0)
    glVertex2f(900.0, 50.0)
    glVertex2f(1050.0, 200.0)
    glVertex2f(1050.0, 500.0)
    glVertex2f(1000.0, 620.0)
    glEnd()

    # Draw boat details
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(750.0, 200.0)
    glVertex2f(1050.0, 200.0)
    glVertex2f(750.0, 350.0)
    glVertex2f(1050.0, 350.0)
    glVertex2f(750.0, 500.0)
    glVertex2f(1050.0, 500.0)
    glEnd()

    glPopMatrix()


def car():
    global g
    glPushMatrix()
    glTranslatef(g, 0, 0)

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(1800.0, 1050.0)
    glVertex2f(1950.0, 1050.0)
    glVertex2f(1950.0, 1150.0)
    glVertex2f(1800.0, 1150.0)
    glEnd()

    # Draw car details
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(1820.0, 1080.0)
    glVertex2f(1920.0, 1080.0)
    glVertex2f(1920.0, 1110.0)
    glVertex2f(1820.0, 1110.0)
    glEnd()

    glPopMatrix()


def poles():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(30.0, 1200.0)
    glVertex2f(50.0, 1200.0)
    glVertex2f(50.0, 1550.0)
    glVertex2f(30.0, 1550.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(1725.0, 1200.0)
    glVertex2f(1745.0, 1200.0)
    glVertex2f(1745.0, 1550.0)
    glVertex2f(1725.0, 1550.0)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    sea()
    bridge()
    boat()
    car()
    poles()


def animate():
    global q, y, i, k, n, g
    q -= 0.5
    y += 0.2
    i += 0.2
    if 135 <= i <= 439:
        k += 0.1
        n += 0.1
    if i >= 1200 and not (k <= 0 and n <= 0):
        k -= 0.1
        n -= 0.1
    if k <= 0:
        g -= 0.5


def main():
    pygame.init()
    window_size = (2000, 1600)
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
    gluOrtho2D(0.0, 2000.0, 0.0, 1600.0)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    global m, j, o
                    m, j, o = 1.0, 0.0, 0.0
                elif event.key == pygame.K_g:
                    m, j, o = 0.0, 1.0, 0.0
                elif event.key == pygame.K_b:
                    m, j, o = 0.80, 0.50, 0.15
                elif event.key == pygame.K_w:
                    m, j, o = 1.0, 1.0, 1.0
                elif event.key == pygame.K_m:
                    m, j, o = 1.0, 0.0, 1.0
                elif event.key == pygame.K_c:
                    m, j, o = 0.0, 1.0, 1.0
                elif event.key == pygame.K_y:
                    m, j, o = 0.75, 0.75, 0.75

        animate()
        display()
        pygame.display.flip()
        clock.tick(60)


if _name_ == "_main_":
    main()