import random as rd


def make_matrix(size):
    result = [[rd.randint(0, 20) for i in range(size)] for j in range(size)]
    return result
