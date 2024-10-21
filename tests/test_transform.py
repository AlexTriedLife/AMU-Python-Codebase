import pygame
import components.transform
import pytest


class TestTransform:
    def testTransformInitialization(self):
        # object to test
        t_transf = components.transform.Transform2D()

        assert t_transf.position.x == 0
        assert t_transf.position.y == 0
        assert t_transf.rotation == 0
        assert t_transf.scale == pygame.Vector2(1, 1)

    @pytest.mark.parametrize(
        "t_scale_x, t_scale_y, t_should_pass",
        [
            # positive tests
            (1, 1, True),
            (2, 1, True),
            (2, 2, True),
            (100, 0, False),
            (0, 100, False),
            # negative tests
            (-1, 0, False),
            (0, -1, False),
            (-1, 1, False),
            (1, -1, False),
            (-1, -1, False),
        ],
    )
    def test_setScale(self, t_scale_x, t_scale_y, t_should_pass):
             t_transf = components.transform.Transform2D((0, 0), 0, (1, 1))
             if t_should_pass:
                  t_transf.set_scale(t_scale_x, t_scale_y)
                  assert t_transf.scale == pygame.Vector2(t_scale_x, t_scale_y)
             else:
                  with pytest.raises(AssertionError):
                       t_transf.set_scale(t_scale_x, t_scale_y)
