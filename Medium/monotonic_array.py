import unittest

# O(n) time | O(1) space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_2(self):
        array = []
        self.assertEqual(isMonotonic(array), True)

    def test_case_3(self):
        array = [1]
        self.assertEqual(isMonotonic(array), True)

    def test_case_4(self):
        array = [1, 2]
        self.assertEqual(isMonotonic(array), True)

    def test_case_5(self):
        array = [2, 1]
        self.assertEqual(isMonotonic(array), True)

    def test_case_6(self):
        array = [1, 5, 10, 1100, 1101, 1102, 9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_7(self):
        array = [-1, -5, -10, -1100, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_8(self):
        array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), False)

    def test_case_9(self):
        array = [1, 2, 0]
        self.assertEqual(isMonotonic(array), False)

    def test_case_10(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
        self.assertEqual(isMonotonic(array), False)

    def test_case_11(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        self.assertEqual(isMonotonic(array), True)

    def test_case_12(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]
        self.assertEqual(isMonotonic(array), False)

    def test_case_13(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
        self.assertEqual(isMonotonic(array), True)
    
    def test_case_14(self):
        array = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(isMonotonic(array), True)

    def test_case_15(self):
        array = [1, 2, -1, -2, -5]
        self.assertEqual(isMonotonic(array), False)

    def test_case_16(self):
        array = [-1, -5, 10]
        self.assertEqual(isMonotonic(array), False)

    def test_case_17(self):
        array = [2, 2, 2, 1, 4, 5]
        self.assertEqual(isMonotonic(array), False)

if __name__ == '__main__':
    unittest.main()
