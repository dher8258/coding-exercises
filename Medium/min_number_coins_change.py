import unittest

def minNumberOfCoinsForChange(n, denoms):
    pass

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        n = 7
        denoms = [1, 5, 10]
        self.assertEqual(minNumberOfCoinsForChange(n, denoms), 3)

if __name__ == '__main__':
    unittest.main()