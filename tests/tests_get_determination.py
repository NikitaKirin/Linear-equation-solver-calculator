import unittest
import core.det as det
import numpy as np  # Библиотека python для работы с матрицами
import core.matrix_generator as gen  # Свой скрипт для генерации рандомных матриц определенного размера


class MyTestCase(unittest.TestCase):
    def test_det_of_2X2_matrix(self):
        matrix = gen.make_matrix(2)
        result = det.get_determination(matrix)
        answer = round(np.linalg.det(matrix))

        self.assertEqual(result, answer)

    def test_det_of_3X3_matrix(self):
        matrix = [
            [3, 1, 5],
            [4, 2, 1],
            [5, 4, 2]
        ]
        result = det.get_determination(matrix)
        answer = np.linalg.det(matrix)

        self.assertEqual(result, answer)

    def test_det_of_4X4_matrix(self):
        matrix = [
            [3, 1, 5, 6],
            [4, 2, 1, 10],
            [5, 4, 2, 5],
            [5, 4, 2, 9],
        ]
        result = det.get_determination(matrix)
        answer = int(np.linalg.det(matrix))

        self.assertEqual(result, answer)

    def test_det_of_5X5_matrix(self):
        matrix = gen.make_matrix(5);
        result = det.get_determination(matrix)
        answer = round(np.linalg.det(matrix))
        self.assertEqual(result, answer)

    def test_det_of_10X10_matrix(self):
        matrix = gen.make_matrix(10);
        result = det.get_determination(matrix)
        answer = round(np.linalg.det(matrix))
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
