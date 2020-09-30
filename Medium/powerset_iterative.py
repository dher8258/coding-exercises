import unittest

"""
The function takes in an array of unique integers and returns its powerset.

The powerset P(X) of a set X is the set of all subsets of X. For example, the
powerset of [1, 2] is [[], [1], [1, 2]].

The sets in the powerset do not need to be in any particular order.
"""

# O(n*2^n) time | O(n*2^n) space
def powerset(array):
	subsets = [[]]
	for element in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [element])
	return subsets

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		output = list(map(lambda x: set(x), powerset([1, 2, 3])))
		self.assertTrue(len(output) == 8)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)
		self.assertTrue(set([2]) in output)
		self.assertTrue(set([1, 2]) in output)
		self.assertTrue(set([3]) in output)
		self.assertTrue(set([1, 3]) in output)
		self.assertTrue(set([2, 3]) in output)
		self.assertTrue(set([1, 2, 3]) in output)

	def test_case_2(self):
		output = list(map(lambda x: set(x), powerset([])))
		self.assertTrue(len(output) == 1)
		self.assertTrue(set([]) in output)

	def test_case_3(self):
		output = list(map(lambda x: set(x), powerset([1])))
		self.assertTrue(len(output) == 2)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)

	def test_case_4(self):
		output = list(map(lambda x: set(x), powerset([1, 2])))
		self.assertTrue(len(output) == 4)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)
		self.assertTrue(set([2]) in output)
		self.assertTrue(set([1, 2]) in output)

	def test_case_5(self):
		output = list(map(lambda x: set(x), powerset([1, 2, 3, 4])))
		self.assertTrue(len(output) == 16)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)
		self.assertTrue(set([2]) in output)
		self.assertTrue(set([1, 2]) in output)
		self.assertTrue(set([3]) in output)
		self.assertTrue(set([1, 3]) in output)
		self.assertTrue(set([2, 3]) in output)
		self.assertTrue(set([1, 2, 3]) in output)
		self.assertTrue(set([4]) in output)
		self.assertTrue(set([1, 4]) in output)
		self.assertTrue(set([2, 4]) in output)
		self.assertTrue(set([1, 2, 4]) in output)
		self.assertTrue(set([3, 4]) in output)
		self.assertTrue(set([1, 3, 4]) in output)
		self.assertTrue(set([2, 3, 4]) in output)
		self.assertTrue(set([1, 2, 3, 4]) in output)

	def test_case_6(self):
		output = list(map(lambda x: set(x), powerset([1, 2, 3, 4, 5])))
		self.assertTrue(len(output) == 32)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)
		self.assertTrue(set([2]) in output)
		self.assertTrue(set([1, 2]) in output)
		self.assertTrue(set([3]) in output)
		self.assertTrue(set([1, 3]) in output)
		self.assertTrue(set([2, 3]) in output)
		self.assertTrue(set([1, 2, 3]) in output)
		self.assertTrue(set([4]) in output)
		self.assertTrue(set([1, 4]) in output)
		self.assertTrue(set([2, 4]) in output)
		self.assertTrue(set([1, 2, 4]) in output)
		self.assertTrue(set([3, 4]) in output)
		self.assertTrue(set([1, 3, 4]) in output)
		self.assertTrue(set([2, 3, 4]) in output)
		self.assertTrue(set([1, 2, 3, 4]) in output)
		self.assertTrue(set([5]) in output)
		self.assertTrue(set([1, 5]) in output)
		self.assertTrue(set([2, 5]) in output)
		self.assertTrue(set([1, 2, 5]) in output)
		self.assertTrue(set([3, 5]) in output)
		self.assertTrue(set([1, 3, 5]) in output)
		self.assertTrue(set([2, 3, 5]) in output)
		self.assertTrue(set([1, 2, 3, 5]) in output)
		self.assertTrue(set([4, 5]) in output)
		self.assertTrue(set([1, 4, 5]) in output)
		self.assertTrue(set([2, 4, 5]) in output)
		self.assertTrue(set([1, 2, 4, 5]) in output)
		self.assertTrue(set([3, 4, 5]) in output)
		self.assertTrue(set([1, 3, 4, 5]) in output)
		self.assertTrue(set([2, 3, 4, 5]) in output)
		self.assertTrue(set([1, 2, 3, 4, 5]) in output)

	def test_case_7(self):
		output = list(map(lambda x: set(x), powerset([1, 2, 3, 4, 5, 6])))
		self.assertTrue(len(output) == 64)
		self.assertTrue(set([]) in output)
		self.assertTrue(set([1]) in output)
		self.assertTrue(set([2]) in output)
		self.assertTrue(set([1, 2]) in output)
		self.assertTrue(set([3]) in output)
		self.assertTrue(set([1, 3]) in output)
		self.assertTrue(set([2, 3]) in output)
		self.assertTrue(set([1, 2, 3]) in output)
		self.assertTrue(set([4]) in output)
		self.assertTrue(set([1, 4]) in output)
		self.assertTrue(set([2, 4]) in output)
		self.assertTrue(set([1, 2, 4]) in output)
		self.assertTrue(set([3, 4]) in output)
		self.assertTrue(set([1, 3, 4]) in output)
		self.assertTrue(set([2, 3, 4]) in output)
		self.assertTrue(set([1, 2, 3, 4]) in output)
		self.assertTrue(set([5]) in output)
		self.assertTrue(set([1, 5]) in output)
		self.assertTrue(set([2, 5]) in output)
		self.assertTrue(set([1, 2, 5]) in output)
		self.assertTrue(set([3, 5]) in output)
		self.assertTrue(set([1, 3, 5]) in output)
		self.assertTrue(set([2, 3, 5]) in output)
		self.assertTrue(set([1, 2, 3, 5]) in output)
		self.assertTrue(set([4, 5]) in output)
		self.assertTrue(set([1, 4, 5]) in output)
		self.assertTrue(set([2, 4, 5]) in output)
		self.assertTrue(set([1, 2, 4, 5]) in output)
		self.assertTrue(set([3, 4, 5]) in output)
		self.assertTrue(set([1, 3, 4, 5]) in output)
		self.assertTrue(set([2, 3, 4, 5]) in output)
		self.assertTrue(set([1, 2, 3, 4, 5]) in output)
		self.assertTrue(set([6]) in output)
		self.assertTrue(set([1, 6]) in output)
		self.assertTrue(set([2, 6]) in output)
		self.assertTrue(set([1, 2, 6]) in output)
		self.assertTrue(set([3, 6]) in output)
		self.assertTrue(set([1, 3, 6]) in output)
		self.assertTrue(set([2, 3, 6]) in output)
		self.assertTrue(set([1, 2, 3, 6]) in output)
		self.assertTrue(set([4, 6]) in output)
		self.assertTrue(set([1, 4, 6]) in output)
		self.assertTrue(set([2, 4, 6]) in output)
		self.assertTrue(set([1, 2, 4, 6]) in output)
		self.assertTrue(set([3, 4, 6]) in output)
		self.assertTrue(set([1, 3, 4, 6]) in output)
		self.assertTrue(set([2, 3, 4, 6]) in output)
		self.assertTrue(set([1, 2, 3, 4, 6]) in output)
		self.assertTrue(set([5, 6]) in output)
		self.assertTrue(set([1, 5, 6]) in output)
		self.assertTrue(set([2, 5, 6]) in output)
		self.assertTrue(set([1, 2, 5, 6]) in output)
		self.assertTrue(set([3, 5, 6]) in output)
		self.assertTrue(set([1, 3, 5, 6]) in output)
		self.assertTrue(set([2, 3, 5, 6]) in output)
		self.assertTrue(set([1, 2, 3, 5, 6]) in output)
		self.assertTrue(set([4, 5, 6]) in output)
		self.assertTrue(set([1, 4, 5, 6]) in output)
		self.assertTrue(set([2, 4, 5, 6]) in output)
		self.assertTrue(set([1, 2, 4, 5, 6]) in output)
		self.assertTrue(set([3, 4, 5, 6]) in output)
		self.assertTrue(set([1, 3, 4, 5, 6]) in output)
		self.assertTrue(set([2, 3, 4, 5, 6]) in output)
		self.assertTrue(set([1, 2, 3, 4, 5, 6]) in output)

if __name__ == '__main__':
	unittest.main()