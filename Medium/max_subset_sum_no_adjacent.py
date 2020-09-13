import unittest

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [75, 105, 120, 75, 90, 135]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 330)

    def test_case_2(self):
        array = []
        self.assertEqual(maxSubsetSumNoAdjacent(array), 0)

    def test_case_3(self):
        array = [1]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 1)

    def test_case_4(self):
        array = [1, 2]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 2)

    def test_case_5(self):
        array = [1, 2, 3]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 4)

    def test_case_6(self):
        array = [1, 15, 3]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 15)

    def test_case_7(self):
        array = [7, 10, 12, 7, 9, 14]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 33)

    def test_case_8(self):
        array = [4, 3, 5, 200, 5, 3]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 207)

    def test_case_9(self):
        array = [10, 5, 20, 25, 15, 5, 5, 15]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 60)

    def test_case_10(self):
        array = [10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 90)

    def test_case_11(self):
        array = [125, 210, 250, 120, 150, 300]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 675)

    def test_case_12(self):
        array = [30, 25, 50, 55, 100]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 180)

    def test_case_13(self):
        array = [30, 25, 50, 55, 100, 120]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 205)

    def test_case_14(self):
        array = [7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]
        self.assertEqual(maxSubsetSumNoAdjacent(array), 72)
        

if __name__ == '__main__':
    unittest.main()	
	