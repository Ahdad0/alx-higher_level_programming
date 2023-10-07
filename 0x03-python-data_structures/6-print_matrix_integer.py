#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    s = ""
    for c in range(0, len(matrix)):
        for r in range(0, len(matrix[c])):
            if r + 1 != len(matrix[c]):
                print("{:d} ".format(matrix[c][r]), end="")
            else:
                print("{:d}".format(matrix[c][r]), end="")
        print()
