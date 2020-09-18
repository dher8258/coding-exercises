import unittest

def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        n = 7
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 3)

    def test_case_2(self):
        n = 0
        denoms = [1, 2, 3]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 0)

    def test_case_3(self):
        n = 3
        denoms = [2, 1]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 2)

    def test_case_4(self):
        n = 4
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 4)

    def test_case_5(self):
        n = 10
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 1)

    def test_case_6(self):
        n = 11
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 2)

    def test_case_7(self):
        n = 24
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 6)

    def test_case_8(self):
        n = 25
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 3)

    def test_case_9(self):
        n = 7
        denoms = [2, 4]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), -1)

    def test_case_10(self):
        n = 7
        denoms = [3, 7]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 1)

    def test_case_11(self):
        n = 9
        denoms = [3, 5]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 3)

    def test_case_12(self):
        n = 9
        denoms = [3, 4, 5]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 2)

    def test_case_13(self):
        n = 135
        denoms = [39, 45, 130, 40, 4, 1, 60, 75]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 2)

    def test_case_14(self):
        n = 10
        denoms = [1, 3, 4]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 3)


if __name__ == '__main__':
    unittest.main()