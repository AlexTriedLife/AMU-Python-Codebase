from typing import Literal
import pytest

# This is really just to get a hang on tests
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a + b

def div(a,b):
    if b == 0:
        assert ZeroDivisionError

    return a / b


class TestMath:
    # paramaters for testing addition
    @pytest.mark.parametrize("tparam_a, tparam_b, texpected_val",[
        (0,0,0),
        (-1,1,0),
        (1,0,1),
        (0,1,1),
        (1,1,2),
        
    ])
    def test_addition(self, tparam_a: Literal[0] | Literal[-1] | Literal[1], tparam_b: Literal[0] | Literal[1], texpected_val: Literal[0] | Literal[1] | Literal[2]):
        assert add(tparam_a, tparam_b) == texpected_val

    # paramaters for testing subtraction
    @pytest.mark.parametrize("tparam_a, tparam_b, texpected_val",[
        (-0,-0,0),
        (1,1,0),
        (-1,-1,0),
        (5,10,-5),
        (0,-1,1),
        
    ])

    def test_subtraction(self, tparam_a: Literal[0] | Literal[1] | Literal[-1] | Literal[5], tparam_b: Literal[0] | Literal[1] | Literal[-1] | Literal[10], texpected_val: Literal[0] | Literal[-5] | Literal[1]):
        assert sub(tparam_a, tparam_b) == texpected_val

    # paramaters for testing division
    @pytest.mark.parametrize("tparam_a, tparam_b, texpected_val",[
        (0,2,0),
        (1,1,1),
        (1,-1,-1),
        (4,2,2),
        (100,10,10),
        
    ])

    def test_division(self, tparam_a: Literal[0] | Literal[1] | Literal[4] | Literal[100], tparam_b: Literal[2] | Literal[1] | Literal[-1] | Literal[10], texpected_val: Literal[0] | Literal[1] | Literal[-1] | Literal[2] | Literal[10]):
        assert div(tparam_a, tparam_b) == texpected_val





