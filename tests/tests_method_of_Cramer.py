import unittest
import core.matrix_generator as gen
import core.method_of_Cramer as calc
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_random_matrix_with_free_variables(self):
        matrix_of_variables = gen.make_matrix(3)
        matrix_free = [[np.random.randint(0, 10) for i in range(1)] for j in range(3)]
        result = calc.method_of_cramer(matrix_of_variables, matrix_free)
        res = np.linalg.solve(matrix_of_variables, matrix_free)
        answer = []
        for i in range(len(res)):
            answer.append(round(res[i][0]))
        self.assertEqual(result, answer)

    def test_random_matrix_with_five_variables(self):
        matrix_of_variables = gen.make_matrix(5)
        matrix_free = [[np.random.randint(0, 10) for i in range(1)] for j in range(5)]
        result = calc.method_of_cramer(matrix_of_variables, matrix_free)
        res = np.linalg.solve(matrix_of_variables, matrix_free)
        answer = []
        for i in range(len(res)):
            answer.append(round(res[i][0]))
        self.assertEqual(result, answer)

    def test_random_matrix_with_ten_variables(self):
        matrix_of_variables = gen.make_matrix(10)
        matrix_free = [[np.random.randint(0, 10) for i in range(1)] for j in range(10)]
        result = calc.method_of_cramer(matrix_of_variables, matrix_free)
        res = np.linalg.solve(matrix_of_variables, matrix_free)
        answer = []
        for i in range(len(res)):
            answer.append(round(res[i][0]))
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
