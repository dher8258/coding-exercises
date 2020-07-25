import unittest

# O(n^2) time | O(1) space
def bubbleSort(array):
    # Write your code here.
	isSorted = False
	counter = 0
	while not isSorted:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array[i+1]:
				swap(i, i +1, array)
				isSorted = False
		counter += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_case_2(self):
        self.assertEqual(bubbleSort([1]), [1])

    def test_case_3(self):
        self.assertEqual(bubbleSort([1, 2]), [1, 2])

    def test_case_4(self):
        self.assertEqual(bubbleSort([2, 1]), [1, 2])

    def test_case_5(self):
        self.assertEqual(bubbleSort([1, 3, 2]), [1, 2, 3])

    def test_case_6(self):
        self.assertEqual(bubbleSort([3, 1, 2]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()