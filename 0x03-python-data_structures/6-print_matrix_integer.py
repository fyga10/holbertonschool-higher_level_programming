#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            a = 0
            for column in row:
                a += 1
                if a == len (row):
                    print("{:d}".format(column))
                else:
                    print("{:d}".format(column), end=" ")
    if len(matrix[0]) == 0:
        print("")
        