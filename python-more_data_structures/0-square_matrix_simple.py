#!/usr/bin/pyhton3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_2 = []
        for x in row:
            row_2.append(x ** 2)
        new_matrix.append(row_2)
    return new_matrix
