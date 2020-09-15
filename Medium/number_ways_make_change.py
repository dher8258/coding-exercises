import unittest

# O(nd) time | O(n) space
# Where 'n' is the target amount and 'd' the number of denominations
def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n + 1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
	return ways[n]

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		n = 6
		denoms = [1, 5]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 2)

	def test_case_2(self):
		n = 0
		denoms = [2, 3, 4, 7]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 1)

	def test_case_3(self):
		n = 9
		denoms = [5]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 0)
	
	def test_case_4(self):
		n = 7
		denoms = [2, 4]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 0)

	def test_case_5(self):
		n = 4
		denoms = [1, 5, 10, 25]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 1)

	def test_case_6(self):
		n = 5
		denoms = [1, 5, 10, 25]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 2)

	def test_case_7(self):
		n = 10
		denoms = [1, 5, 10, 25]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 4)

	def test_case_8(self):
		n = 25
		denoms = [1, 5, 10, 25]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 13)

	def test_case_9(self):
		n = 12
		denoms = [2, 3, 7]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 4)

	def test_case_10(self):
		n = 7
		denoms = [2, 3, 4, 7]
		self.assertEqual(numberOfWaysToMakeChange(n, denoms), 3)


if __name__ == '__main__':
    unittest.main()