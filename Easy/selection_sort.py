import unittest

# O(n^2) time | O(1) space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_case_2(self):
        self.assertEqual(selectionSort([1]), [1])

    def test_case_3(self):
        self.assertEqual(selectionSort([1, 2]), [1, 2])

    def test_case_4(self):
        self.assertEqual(selectionSort([2, 1]), [1, 2])

    def test_case_5(self):
        self.assertEqual(selectionSort([1, 3, 2]), [1, 2, 3])

    def test_case_6(self):
        self.assertEqual(selectionSort([3, 1, 2]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()