#!/usr/bin/python3
""" a function that squares all the values in a matrix """


def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x * x, i)) for i in matrix]
