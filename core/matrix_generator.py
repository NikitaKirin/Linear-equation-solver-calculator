import random as rd


# def make_matrix(size):
#     result = []
#     for i in range(size):
#         temp_array = []
#         for j in range(size):
#             temp_array.append(rd.randint(0, 10))
#         result.append(temp_array)
#
#     return result


def make_matrix(size):
    result = [[rd.randint(0, 20) for i in range(size)] for j in range(size)]
    return result

