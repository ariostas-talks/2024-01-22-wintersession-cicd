from pytest import approx
import numpy as np
from wintersession2024cicd import square_plus_one, exp_minus_one

def test_square_plus_one():
    assert square_plus_one(0) == 1
    assert square_plus_one(1) == 2
    assert square_plus_one(2) == 5
    
    l = np.arange(100)
    l2p1 = square_plus_one(l)
    assert all(c == (i**2)+1 for i,c in enumerate(l2p1))

    l = np.arange(10, step=0.2)
    l2p1 = square_plus_one(l)
    assert all(c == approx(((i*0.2)**2)+1) for i,c in enumerate(l2p1))


def test_exp_minus_one():
    assert exp_minus_one(0) == approx(0)
    assert exp_minus_one(1) == approx(np.e - 1)
    assert exp_minus_one(2) == approx(np.e**2 - 1)
    
    l = np.arange(10)
    elm1 = exp_minus_one(l)
    assert all(c == approx(np.exp(i)-1) for i,c in enumerate(elm1))

    l = np.arange(10, step=0.2)
    elm1 = exp_minus_one(l)
    assert all(c == approx(np.exp(i*0.2)-1) for i,c in enumerate(elm1))
