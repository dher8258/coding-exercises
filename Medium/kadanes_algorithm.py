import unittest

def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        expected = 19
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 55
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_3(self):
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        expected = -1
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_4(self):
        array = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
        expected = -1
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_5(self):
        array = [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]
        expected = 35
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_6(self):
        array = [1, 2, 3, 4, 5, 6, -22, 7, 8, 9, 10]
        expected = 34
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_7(self):
        array = [1, 2, -4, 3, 5, -9, 8, 1, 2]
        expected = 11
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_8(self):
        array = [3, 4, -6, 7, 8]
        expected = 16
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_9(self):
        array = [3, 4, -6, 7, 8, -18, 100]
        expected = 100
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_10(self):
        array = [3, 4, -6, 7, 8, -15, 100]
        expected = 101
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_11(self):
        array = [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        expected = 23
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_12(self):
        array = [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 6]
        expected = 24
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_13(self):
        array = [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6]
        expected = 22
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_14(self):
        array = [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]
        expected = 35
        self.assertEqual(kadanesAlgorithm(array), expected)  

    def test_case_15(self):
        array = [100, 8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]
        expected = 135
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_16(self):
        array = [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]
        expected = 6
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_17(self):
        array = [-2, -1]
        expected = -1
        self.assertEqual(kadanesAlgorithm(array), expected)

    def test_case_18(self):
        array = [-2, 1]
        expected = 1
        self.assertEqual(kadanesAlgorithm(array), expected)   


if __name__ == '__main__':
    unittest.main()