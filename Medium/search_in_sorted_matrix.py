import unittest

"""
Given a two-dimensional array (a matrix) of distinct integers and a target
integer. Each row in the matrix is sorted, and each column is also sorted;
the matrix doesn't necessarily have the same height and width.

The function returns an array of the row and column indices of the target
integer if it's contained in the matrix, otherwise [-1, -1].
"""

# O(n + m) time | O(1) space
def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row, col]																																			
	return [-1, -1]

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
			[2, 5, 19, 31, 32, 1001],
			[3, 8, 24, 33, 35, 1002],
			[40, 41, 42, 44, 45, 1003],
			[99, 100, 103, 106, 128, 1004],
		]
		actual = searchInSortedMatrix(matrix, 44)
		self.assertEqual(actual, [3, 3])

	def test_case_2(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 1)
		self.assertEqual(actual, [0, 0])

	def test_case_3(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 2)
		self.assertEqual(actual, [1, 0])

	def test_case_4(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 4)
		self.assertEqual(actual, [0, 1])

	def test_case_5(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 15)
		self.assertEqual(actual, [0, 4])

	def test_case_6(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 12)
		self.assertEqual(actual, [0, 3])

	def test_case_7(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 32)
		self.assertEqual(actual, [1, 4])

	def test_case_8(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 99)
		self.assertEqual(actual, [4, 0])

	def test_case_9(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 100)
		self.assertEqual(actual, [4, 1])

	def test_case_10(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 40)
		self.assertEqual(actual, [3, 0])

	def test_case_11(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 128)
		self.assertEqual(actual, [4, 4])

	def test_case_12(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 106)
		self.assertEqual(actual, [4, 3])

	def test_case_13(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 45)
		self.assertEqual(actual, [3, 4])

	def test_case_14(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 24)
		self.assertEqual(actual, [2, 2])

	def test_case_15(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 43)
		self.assertEqual(actual, [-1, -1])

	def test_case_16(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, -1)
		self.assertEqual(actual, [-1, -1])

	def test_case_17(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 1000)
		self.assertEqual(actual, [0, 5])

	def test_case_18(self):
		matrix = [
			[1, 4, 7, 12, 15, 1000],
    		[2, 5, 19, 31, 32, 1001],
    		[3, 8, 24, 33, 35, 1002],
    		[40, 41, 42, 44, 45, 1003],
    		[99, 100, 103, 106, 128, 1004]
		]
		actual = searchInSortedMatrix(matrix, 1004)
		self.assertEqual(actual, [4, 5])


if __name__ == '__main__':
	unittest.main()