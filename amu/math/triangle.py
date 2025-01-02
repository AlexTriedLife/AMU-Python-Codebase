import math
from math import radians
from operator import indexOf, index

import numpy as np


class Triangle:
    def __init__(self, angles):
        self.angles = np.array([angles[0],angles[1],angles[2]])
        self.vertices = np.ndarray(shape=(3,2),dtype=float, order="C")
        self.sides = np.array([None,None,None])
        self.right_angles = []
        self.right_angle = self.has_right_angle()
        self.id = self.identify_triangle()
        print(self.right_angles)

    def has_right_angle(self):
        is_right = False
        for angle in self.angles:
            if angle == 90:
                is_right = True
                self.right_angles.append(index(angle))

        return is_right

    def validate_triangle(self):
        angle_sum =  self.angles[0] + self.angles[1] + self.angles[2]
        if angle_sum != 180:
            return False
        for angle in self.angles:
            if angle < 1:
                return False
            elif angle >= 179:
                return False



        return True

    def identify_triangle(self):
        triangle_type = None
        # scalene
        if self.sides[0] != self.sides[1] and self.sides[0] != self.sides[2] and self.sides[1] != self.sides[2]:
            triangle_type = 'scalene'
        return triangle_type


    # def calculate_sides(self):

    # def solve_side_a(self):
    #     self.sides[0] = math.sin()
    # def solve_side_b(self):
    # def solve_side_c(self):

