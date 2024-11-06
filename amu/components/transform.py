import pygame
import math

class Transform2D:
    def __init__(self, position=(0,0), rotation=0, scale=(1,1)): 
        self.position = pygame.Vector2(position)
        self.rotation = math.radians(rotation)
        self.scale = pygame.Vector2(scale)

    def translate(self,x,y):
        self.position += pygame.Vector2(x,y)
    
    def rotate(self, angle):
        self.rotation += math.radians(angle)
        # Limit to 360 degrees(tau)
        self.rotation %= math.tau

    def set_scale(self, x, y):
        assert x > 0 and y > 0, "Scale values must be greater than 0" 
        self.scale = pygame.Vector2(x,y)
    def reset(self):
        self.position = (0,0)
        self.rotation = 0
        self.scale = pygame.Vector2(1,1)

        
    