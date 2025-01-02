import numpy as np
import pytest
from numpy.ma.core import angle

import amu.math.triangle


class TestTriangle:

    @pytest.mark.parametrize(
        "angle_a, angle_b, angle_c, test_should_pass",
        [
            (90, 50, 40, True),
            (30, 90, 60, True),
            (45, 45, 90, True),
            (90, 50, 40, True),
            (60, 10, 110, False),
            (80, 80, 20, False)
        ],
    )
    def test_right_angle(self,angle_a, angle_b, angle_c, test_should_pass):
        test_triangle = amu.math.triangle.Triangle([angle_a,angle_b,angle_c])
        assert test_triangle.right_angle == test_should_pass
    @pytest.mark.parametrize(
        "angle_a, angle_b, angle_c, test_should_pass",
        [
            (90, 50, 40, True),
            (30, 90, 60, True),
            (45, 45, 90, True),
            (90, 50, 40, True),
            (70, 10, 110, False),
            (0, 0, 180, False)
        ],
    )
    def test_angle_validity(self,angle_a, angle_b, angle_c, test_should_pass):
        test_triangle = amu.math.triangle.Triangle([angle_a,angle_b,angle_c])
        assert test_triangle.validate_triangle() == test_should_pass



