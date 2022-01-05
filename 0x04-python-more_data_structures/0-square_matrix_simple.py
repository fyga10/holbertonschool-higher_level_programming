#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = [[item ** 2 for item in i] for i in matrix]
        return new_matrix
