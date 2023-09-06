import math
import unittest

import numpy as np

from Main import main
from MyTestGraphs import *


class MyTestCase(unittest.TestCase):
    def test_H_3X3(self):
        t_V = np.array([[6], [5], [3]])
        R, I = main.get_R_I(DIRECTED_H_3X3_Simple.H)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_A(self):
        t_V = np.array([[1], [1/3], [1/3]])
        R, I = main.get_R_I(DIRECTED_Set1_A.A)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_A_SUPERNODE(self):
        t_V = np.array([[2/3], [0], [-1/3]])
        R, I = main.get_R_I(DIRECTED_Set1_A_SUPERNODE.A)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_B_CS(self):
        t_V = np.array([[0], [4/3], [-8/3]])
        R, I = main.get_R_I(DIRECTED_Set1_B_CS.B)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_C_VSandCS(self):
        t_V = np.array([[2], [0.947368], [-0.526315], [1.578947], [-0.263157]])
        R, I = main.get_R_I(DIRECTED_Set1_C_VSandCS.C)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_E_MULTIPLE_VSandCS(self):
        t_V = np.array([[1], [-1], [-3], [-7], [0]])
        R, I = main.get_R_I(DIRECTED_Set1_E_MULTIPLE_VSandCS.E)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_F_MULTIPLE_VSandCS(self):
        t_V = np.array([[3], [0.6], [0.2], [4], [1]])
        R, I = main.get_R_I(DIRECTED_Set1_F_MULTIPLE_VSandCS.F)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_I_NOOR(self):
        t_V = np.array([[0.62962963], [3], [2.15740741], [1.15740741], [1.36111111]])
        R, I = main.get_R_I(DIRECTED_Set1_I_NOOR.N)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)

    def test_Set1_I_SUPERNODE(self):
        t_V = np.array([[-0.52777778], [0.2037037], [1.84259259], [-1.15740741], [1]])
        R, I = main.get_R_I(DIRECTED_Set1_I_SUPERNODE.I)
        V = main.find_v(R, I)
        test = check_matrix_equality(t_V, V)
        self.assertEqual(test, True)


if __name__ == '__main__':
    unittest.main()


def check_matrix_equality(m1, m2):
    """
    Check if two matrices are equal.
    Only works on Nx1 matrices
    """
    # Check if the matrices have the same shape
    if m1.shape != m2.shape:
        return False

    # Check if each element in the matrices is equal
    for i in range(m1.shape[0]):
        if not math.isclose(m1[i][0], m2[i][0], rel_tol=1e-5):
            return False

    return True

