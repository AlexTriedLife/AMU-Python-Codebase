import math

from OpenGL.GL import *


class elipse:
    def __init__(self, screen, radius_x, radius_y, num_segments):
        self.screen = screen
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.num_segments = num_segments
    def draw_elipse(self):
        glBegin(GL_LINE_LOOP) # Wireframe
        for i in range(self.num_segments):

            # theta
            angle = 2.0 * math.pi * i / self.num_segments
            x = self.radius_x *  math.cos(angle)
            y = self.radius_y * math.sin(angle)
            glVertex(x,y)
        glEnd()
