import math
from operator import contains

import numpy as np
import pytest
from numpy.ma.testutils import assert_equal


class Triangle:
    def __init__(self, angles):
        self.angles = angles
        self.vertices = np.ndarray(shape=(3,2),dtype=float, order="C")
        self.sides = [None] * 3
        self.right_angle = self.has_right_angle()
        self.id = self.identify_triangle()

    def has_right_angle(self):
        # yield True if it's a right triangle
        if 90 in self.angles:
            return True
        else:
            return False

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


