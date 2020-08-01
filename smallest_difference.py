import unittest

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [-1, 5, 10, 20, 28, 3]
        arrayTwo = [26, 134, 135, 15, 17]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [28, 26])

    def test_case_2(self):
        arrayOne = [-1, 5, 10, 20, 3]
        arrayTwo = [26, 134, 135, 15, 17]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [20, 17])

    def test_case_3(self):
        arrayOne = [10, 0, 20, 25]
        arrayTwo = [1005, 1006, 1014, 1032, 1031]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [25, 1005])

    def test_case_4(self):
        arrayOne = [10, 0, 20, 25, 2200]
        arrayTwo = [1005, 1006, 1014, 1032, 1031]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [25, 1005])

    def test_case_5(self):
        arrayOne = [10, 0, 20, 25, 2000]
        arrayTwo = [1005, 1006, 1014, 1032, 1031]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [2000, 1032])

    def test_case_6(self):
        arrayOne = [240, 124, 86, 111, 2, 84, 954, 27, 89]
        arrayTwo = [1, 3, 954, 19, 8]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [954, 954])

    def test_case_7(self):
        arrayOne = [0, 20]
        arrayTwo = [21, -2]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [20, 21])

    def test_case_8(self):
        arrayOne = [10, 1000]
        arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [1000, 1014])

    def test_case_9(self):
        arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
        arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [-123, -124])

    def test_case_10(self):
        arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530]
        arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
        self.assertEqual(smallestDifference(arrayOne, arrayTwo), [530, 530])

if __name__ == '__main__':
    unittest.main()