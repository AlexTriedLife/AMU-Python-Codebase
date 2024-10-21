import pygame
from pygame.locals import *


class gameApp:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.display = (screen_width, screen_height)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)

