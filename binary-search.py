import unittest

# O(log(n)) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right)//2
        potentialMatch = array[middle]
        if target < potentialMatch:
            right = middle - 1
        elif target > potentialMatch:
            left = middle + 1
        else:
            return middle
    return -1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        self.assertEqual(binarySearch(array, 33), 3)

    def test_case_2(self):
        array = [1, 5, 23, 111]
        self.assertEqual(binarySearch(array, 111), 3)

    def test_case_3(self):
        array = [1, 5, 23, 111]
        self.assertEqual(binarySearch(array, 5), 1)

    def test_case_4(self):
        array = [1, 5, 23, 111]
        self.assertEqual(binarySearch(array, 35), -1)

    def test_case_5(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        self.assertEqual(binarySearch(array, 72), 8)

    def test_case_6(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        self.assertEqual(binarySearch(array, 73), 9)

    def test_case_7(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        self.assertEqual(binarySearch(array, 70), -1)

    def test_case_8(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        self.assertEqual(binarySearch(array, 355), 10)

    def test_case_9(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        self.assertEqual(binarySearch(array, 354), -1)

    def test_case_10(self):
        array = [1, 5, 23, 111]
        self.assertEqual(binarySearch(array, 120), -1) 

    def test_case_11(self):
        array = [5, 23, 111]
        self.assertEqual(binarySearch(array, 3), -1)   

if __name__ == '__main__':
    unittest.main()