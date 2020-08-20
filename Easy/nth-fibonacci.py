import unittest

# O(n) time | O(1) space
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3

    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1

    return lastTwo[1] if n > 1 else lastTwo[0]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(6), 5)

    def test_case_2(self):
        self.assertEqual(getNthFib(2), 1)

    def test_case_3(self):
        self.assertEqual(getNthFib(7), 8)

    def test_case_4(self):
        self.assertEqual(getNthFib(1), 0)

if __name__ == '__main__':
    unittest.main()
