from amu.graphics.gl_shapes import *
from amu.graphics.screen import *
import pygame
from pygame import locals
from amu.components.transform import Transform2D
import OpenGL.GL as GL
import OpenGL.GLU as GLU


class Bird:
    def __init__(self, display):
        self.sprite = elipse(display, 50, 20, 50)
        self.transform = Transform2D()

    def render(self):
        GL.glColor3f(255, 255, 0)
        self.sprite.draw_elipse()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bird = Bird(self.screen)
        self.main_loop()

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.clear()
            self.bird.render()
            screen.update()


if __name__ == '__main__':
    screen = Screen(800, 600)
    game = Game(screen)
