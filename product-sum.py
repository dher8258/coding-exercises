import unittest

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]), 12)

    def test_case_2(self):
        self.assertEqual(productSum([1, 2, 3, 4, 5]), 15)

    def test_case_3(self):
        self.assertEqual(productSum([1, 2, [3], 4, 5]), 18)

    def test_case_4(self):
        self.assertEqual(productSum([[1, 2], 3, [4, 5]]), 27)

    def test_case_5(self):
        self.assertEqual(productSum([[[[[5]]]]]), 600)

    def test_case_6(self):
        array = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], \
            [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], \
            [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
            [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2, ]], [1, -3, 2]]], \
            -3]
        self.assertEqual(productSum(array), 1351)

if __name__ == '__main__':
    unittest.main()