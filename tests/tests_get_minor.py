import unittest
import core.det as det


class MyTestCase(unittest.TestCase):
    def test_minor_2X2(self):
        matrix = [
            [3, 1, 5],
            [4, 2, 1],
            [5, 4, 2]
        ]
        result = det.get_minor(matrix, 1, 1)
        answer = [
            [3, 5],
            [5, 2]
        ]
        self.assertEqual(result, answer)

    def test_minor_3X3(self):
        matrix = [
            [3, 1, 5, 6],
            [4, 2, 1, 2],
            [5, 4, 2, 4],
            [2, 1, 5, 8]
        ]
        result = det.get_minor(matrix, 1, 1)
        answer = [
            [3, 5, 6],
            [5, 2, 4],
            [2, 5, 8]
        ]
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
