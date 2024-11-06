import pygame
from pygame.locals import *
import OpenGL.GL as GL
import OpenGL.GLU as GLU


class Screen:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.display = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        self.setup_opengl()

    def setup_opengl(self):
        """
        setup ortho view with screen edges
        :parameters x1, x2, y1, y2
        """
        GLU.gluOrtho2D(-self.width // 2, self.width // 2, -self.height // 2, self.height // 2)
    def clear(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    def update(self):
        # Swap buffers
        pygame.display.flip()
        pygame.time.wait(10)  # frame rate
