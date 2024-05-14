#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for i, num in enumerate(array):
            if i == len(array) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()
