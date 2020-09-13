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

if __name__ == '__main__':
    unittest.main()