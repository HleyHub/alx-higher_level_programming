#!/usr/bin/python3

"""
A function that divides a matrix
Args: matrix, div
The matrix must be a list of lists of integers/floats,
otherwise raise a TypeError
"""

def matrix_divided(matrix, div):
   """
   Return: matrix / div
   """
   
   errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
   if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
       raise TypeError(errorMessage)
   if not isinstance(div, int) and not isinstance(div, float):
       raise TypeError("div must be a number")
   if not matrix:
       raise TypeError(errorMessage)
   if div == 0:
       raise ZeroDivisionError("division by zero")
   row_size = len(matrix[0])
   if not all(len(row) == row_size for row in matrix):
       raise TypeError("Each row of the matrix must have the same size")
   return [[round(item / div, 2) for item in lists] for lists in matrix]
