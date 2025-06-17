import math
import numpy as np
import sys
import os

# Add the parent directory to sys.path so Python can find 'tests'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import main
from tests.test_circuits import *

def check_matrix_equality(m1, m2):
    """Check if two matrices are equal. Only works on Nx1 matrices."""
    if m1.shape != m2.shape:
        return False
    for i in range(m1.shape[0]):
        if not math.isclose(m1[i][0], m2[i][0], rel_tol=1e-5):
            return False
    return True

def test_h_3x3():
    t_V = np.array([[6], [5], [3]])
    R, I = main.get_R_I(directed_h_3x3_simple())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_a():
    t_V = np.array([[1], [1/3], [1/3]])
    R, I = main.get_R_I(directed_set1_a())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_a_supernode():
    t_V = np.array([[2/3], [0], [-1/3]])
    R, I = main.get_R_I(directed_set1_a_supernode())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_b_cs():
    t_V = np.array([[0], [4/3], [-8/3]])
    R, I = main.get_R_I(directed_set1_b_cs())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_c_vsandcs():
    t_V = np.array([[2], [0.947368], [-0.526315], [1.578947], [-0.263157]])
    R, I = main.get_R_I(directed_set1_c_vsandcs())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_e_multiple_vsandcs():
    t_V = np.array([[1], [-1], [-3], [-7], [0]])
    R, I = main.get_R_I(directed_set1_e_multiple_vsandcs())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_f_multiple_vsandcs():
    t_V = np.array([[3], [0.6], [0.2], [4], [1]])
    R, I = main.get_R_I(directed_set1_f_multiple_vsandcs())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_i_noor():
    t_V = np.array([[0.62962963], [3], [2.15740741], [1.15740741], [1.36111111]])
    R, I = main.get_R_I(directed_set1_i_noor())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)

def test_set1_i_supernode():
    t_V = np.array([[-0.52777778], [0.2037037], [1.84259259], [-1.15740741], [1]])
    R, I = main.get_R_I(directed_set1_i_supernode())
    V = main.find_v(R, I)
    assert check_matrix_equality(t_V, V)
