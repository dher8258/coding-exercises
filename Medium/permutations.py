import unittest

"""
Function that takes in an array of unique integers and returns and array of all
permutations of those integers in no particular order.

When the input arrray is empty, the function returns an empty array.
"""

# O(n*n!) time | O(n*n!) space
def getPermutations(array):
	permutations = []
	permutationsHelper(0, array, permutations)
	return permutations

def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i, j)
			permutationsHelper(i + 1, array, permutations)
			swap(array, i, j)
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		perms = getPermutations([1, 2, 3])
		self.assertTrue(len(perms) == 6)
		self.assertTrue([1, 2, 3] in perms)
		self.assertTrue([1, 3, 2] in perms)
		self.assertTrue([2, 1, 3] in perms)
		self.assertTrue([2, 3, 1] in perms)
		self.assertTrue([3, 1, 2] in perms)
		self.assertTrue([3, 2, 1] in perms)

	def test_case_2(self):
		perms = getPermutations([])
		self.assertTrue(len(perms) == 0)

	def test_case_3(self):
		perms = getPermutations([1])
		self.assertTrue(len(perms) == 1)
		self.assertTrue([1] in perms)

	def test_case_4(self):
		perms = getPermutations([1, 2])
		self.assertTrue(len(perms) == 2)
		self.assertTrue([1, 2] in perms)
		self.assertTrue([2, 1] in perms)

	def test_case_5(self):
		perms = getPermutations([1, 2, 3, 4])
		self.assertTrue(len(perms) == 24)
		self.assertTrue([1, 2, 3, 4] in perms)
		self.assertTrue([1, 2, 4, 3] in perms)
		self.assertTrue([1, 3, 2, 4] in perms)
		self.assertTrue([1, 3, 4, 2] in perms)
		self.assertTrue([1, 4, 3, 2] in perms)
		self.assertTrue([1, 4, 2, 3] in perms)
		self.assertTrue([2, 1, 3, 4] in perms)
		self.assertTrue([2, 1, 4, 3] in perms)
		self.assertTrue([2, 3, 1, 4] in perms)
		self.assertTrue([2, 3, 4, 1] in perms)
		self.assertTrue([2, 4, 3, 1] in perms)
		self.assertTrue([2, 4, 1, 3] in perms)
		self.assertTrue([3, 2, 1, 4] in perms)
		self.assertTrue([3, 2, 4, 1] in perms)
		self.assertTrue([3, 1, 2, 4] in perms)
		self.assertTrue([3, 1, 4, 2] in perms)
		self.assertTrue([3, 4, 1, 2] in perms)
		self.assertTrue([3, 4, 2, 1] in perms)
		self.assertTrue([4, 2, 3, 1] in perms)
		self.assertTrue([4, 2, 1, 3] in perms)
		self.assertTrue([4, 3, 2, 1] in perms)
		self.assertTrue([4, 3, 1, 2] in perms)
		self.assertTrue([4, 1, 3, 2] in perms)
		self.assertTrue([4, 1, 2, 3] in perms)

def test_case_6(self):
		perms = getPermutations([1, 2, 3, 4, 5])
		self.assertTrue(len(perms) == 120)
		self.assertTrue([1, 2, 3, 4, 5] in perms)
		self.assertTrue([1, 2, 3, 5, 4] in perms)
		self.assertTrue([1, 2, 4, 3, 5] in perms)
		self.assertTrue([1, 2, 4, 5, 3] in perms)
		self.assertTrue([1, 2, 5, 4, 3] in perms)
		self.assertTrue([1, 2, 5, 3, 4] in perms)
		self.assertTrue([1, 3, 2, 4, 5] in perms)
		self.assertTrue([1, 3, 2, 5, 4] in perms)
		self.assertTrue([1, 3, 4, 2, 5] in perms)
		self.assertTrue([1, 3, 4, 5, 2] in perms)
		self.assertTrue([1, 3, 5, 4, 2] in perms)
		self.assertTrue([1, 3, 5, 2, 4] in perms)
		self.assertTrue([1, 4, 3, 2, 5] in perms)
		self.assertTrue([1, 4, 3, 5, 2] in perms)
		self.assertTrue([1, 4, 2, 3, 5] in perms)
		self.assertTrue([1, 4, 5, 2, 3] in perms)
		self.assertTrue([1, 4, 5, 3, 2] in perms)
		self.assertTrue([1, 5, 3, 4, 2] in perms)
		self.assertTrue([1, 5, 3, 2, 4] in perms)
		self.assertTrue([1, 5, 4, 3, 2] in perms)
		self.assertTrue([1, 5, 4, 2, 3] in perms)
		self.assertTrue([1, 5, 2, 4, 3] in perms)
		self.assertTrue([1, 5, 2, 3, 4] in perms)
		self.assertTrue([2, 1, 3, 4, 5] in perms)
		self.assertTrue([2, 1, 3, 5, 4] in perms)
		self.assertTrue([2, 1, 4, 3, 5] in perms)
		self.assertTrue([2, 1, 4, 5, 3] in perms)
		self.assertTrue([2, 1, 5, 4, 3] in perms)
		self.assertTrue([2, 1, 5, 3, 4] in perms)
		self.assertTrue([2, 3, 1, 4, 5] in perms)
		self.assertTrue([2, 3, 1, 5, 4] in perms)
		self.assertTrue([2, 3, 4, 1, 5] in perms)
		self.assertTrue([2, 3, 4, 5, 1] in perms)
		self.assertTrue([2, 3, 5, 4, 1] in perms)
		self.assertTrue([2, 3, 5, 1, 4] in perms)
		self.assertTrue([2, 4, 3, 1, 5] in perms)
		self.assertTrue([2, 4, 3, 5, 1] in perms)
		self.assertTrue([2, 4, 1, 3, 5] in perms)
		self.assertTrue([2, 4, 1, 5, 3] in perms)
		self.assertTrue([2, 4, 5, 1, 3] in perms)
		self.assertTrue([2, 4, 5, 3, 1] in perms)
		self.assertTrue([2, 5, 3, 4, 1] in perms)
		self.assertTrue([2, 5, 3, 1, 4] in perms)
		self.assertTrue([2, 5, 4, 3, 1] in perms)
		self.assertTrue([2, 5, 4, 1, 3] in perms)
		self.assertTrue([2, 5, 1, 4, 3] in perms)
		self.assertTrue([2, 5, 1, 3, 4] in perms)
		self.assertTrue([3, 2, 1, 4, 5] in perms)
		self.assertTrue([3, 2, 1, 5, 4] in perms)
		self.assertTrue([3, 2, 4, 1, 5] in perms)
		self.assertTrue([3, 2, 4, 5, 1] in perms)
		self.assertTrue([3, 2, 5, 4, 1] in perms)
		self.assertTrue([3, 2, 5, 1, 4] in perms)
		self.assertTrue([3, 1, 2, 4, 5] in perms)
		self.assertTrue([3, 1, 2, 5, 4] in perms)
		self.assertTrue([3, 1, 4, 2, 5] in perms)
		self.assertTrue([3, 1, 4, 5, 2] in perms)
		self.assertTrue([3, 1, 5, 4, 2] in perms)
		self.assertTrue([3, 1, 5, 2, 4] in perms)
		self.assertTrue([3, 1, 5, 2, 4] in perms)
		self.assertTrue([3, 4, 1, 2, 5] in perms)
		self.assertTrue([3, 4, 1, 5, 2] in perms)
		self.assertTrue([3, 4, 2, 1, 5] in perms)
		self.assertTrue([3, 4, 2, 5, 1] in perms)
		self.assertTrue([3, 4, 5, 2, 1] in perms)
		self.assertTrue([3, 4, 5, 2, 1] in perms)
		self.assertTrue([3, 4, 5, 1, 2] in perms)
		self.assertTrue([3, 5, 1, 4, 2] in perms)
		self.assertTrue([3, 5, 1, 2, 4] in perms)
		self.assertTrue([3, 5, 4, 1, 2] in perms)
		self.assertTrue([3, 5, 4, 2, 1] in perms)
		self.assertTrue([3, 5, 2, 4, 1] in perms)
		self.assertTrue([3, 5, 2, 1, 4] in perms)
		self.assertTrue([4, 2, 3, 1, 5] in perms)
		self.assertTrue([4, 2, 3, 5, 1] in perms)
		self.assertTrue([4, 2, 1, 3, 5] in perms)
		self.assertTrue([4, 2, 1, 5, 3] in perms)
		self.assertTrue([4, 2, 5, 1, 3] in perms)
		self.assertTrue([4, 2, 5, 3, 1] in perms)
		self.assertTrue([4, 3, 2, 1, 5] in perms)
		self.assertTrue([4, 3, 2, 5, 1] in perms)
		self.assertTrue([4, 3, 1, 2, 5] in perms)
		self.assertTrue([4, 3, 1, 5, 2] in perms)
		self.assertTrue([4, 3, 5, 1, 2] in perms)
		self.assertTrue([4, 3, 5, 2, 1] in perms)
		self.assertTrue([4, 1, 3, 2, 5] in perms)
		self.assertTrue([4, 1, 3, 5, 2] in perms)
		self.assertTrue([4, 1, 2, 3, 5] in perms)
		self.assertTrue([4, 1, 2, 5, 3] in perms)
		self.assertTrue([4, 1, 5, 2, 3] in perms)
		self.assertTrue([4, 1, 5, 3, 2] in perms)
		self.assertTrue([4, 5, 3, 1, 2] in perms)
		self.assertTrue([4, 5, 3, 2, 1] in perms)
		self.assertTrue([4, 5, 1, 3, 2] in perms)
		self.assertTrue([4, 5, 1, 2, 3] in perms)
		self.assertTrue([4, 5, 2, 1, 3] in perms)
		self.assertTrue([4, 5, 2, 3, 1] in perms)
		self.assertTrue([5, 2, 3, 4, 1] in perms)
		self.assertTrue([5, 2, 3, 1, 4] in perms)
		self.assertTrue([5, 2, 4, 3, 1] in perms)
		self.assertTrue([5, 2, 4, 1, 3] in perms)
		self.assertTrue([5, 2, 1, 4, 3] in perms)
		self.assertTrue([5, 2, 1, 3, 4] in perms)
		self.assertTrue([5, 3, 2, 4, 1] in perms)
		self.assertTrue([5, 3, 2, 1, 4] in perms)
		self.assertTrue([5, 3, 4, 2, 1] in perms)
		self.assertTrue([5, 3, 4, 1, 2] in perms)
		self.assertTrue([5, 3, 1, 4, 2] in perms)
		self.assertTrue([5, 3, 1, 2, 4] in perms)
		self.assertTrue([5, 4, 3, 2, 1] in perms)
		self.assertTrue([5, 4, 3, 1, 2] in perms)
		self.assertTrue([5, 4, 2, 3, 1] in perms)
		self.assertTrue([5, 4, 2, 1, 3] in perms)
		self.assertTrue([5, 4, 1, 2, 3] in perms)
		self.assertTrue([5, 4, 1, 3, 2] in perms)
		self.assertTrue([5, 1, 3, 4, 2] in perms)
		self.assertTrue([5, 1, 3, 2, 4] in perms)
		self.assertTrue([5, 1, 4, 3, 2] in perms)
		self.assertTrue([5, 1, 4, 2, 3] in perms)
		self.assertTrue([5, 1, 4, 2, 3] in perms)
		self.assertTrue([5, 1, 2, 4, 3] in perms)
		self.assertTrue([5, 1, 2, 3, 4] in perms)  


if __name__ == '__main__':
	unittest.main()