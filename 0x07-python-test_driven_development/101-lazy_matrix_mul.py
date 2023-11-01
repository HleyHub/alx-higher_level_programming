#!/usr/bin/python3
"""
Multiplication of 2 matrices using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices
    """

    result_mult = np.dot(m_a, m_b)
    return result_mult
