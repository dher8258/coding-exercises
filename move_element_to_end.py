import unittest

# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    idxLeft = 0
    idxRight = len(array) - 1
    while idxLeft < idxRight:
        if array[idxRight] == toMove:
            idxRight -= 1
        else:
            if array[idxLeft] == toMove:
                swap(array, idxLeft, idxRight)
                idxRight -= 1
            else:
                idxLeft += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        initialArray = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        arrayExpected = [4, 1, 3, 2, 2, 2, 2, 2]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_2(self):
        initialArray = []
        toMove = 3
        arrayExpected = []
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_3(self):
        initialArray = [1, 2, 4, 5, 6]
        toMove = 3
        arrayExpected = [1, 2, 4, 5, 6]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_4(self):
        initialArray = [3, 3, 3, 3, 3]
        toMove = 3
        arrayExpected = [3, 3, 3, 3, 3]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_5(self):
        initialArray = [3, 1, 2, 4, 5]
        toMove = 3
        arrayExpected = [5, 1, 2, 4, 3]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_6(self):
        initialArray = [1, 2, 4, 5, 3]
        toMove = 3
        arrayExpected = [1, 2, 4, 5, 3]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_7(self):
        initialArray = [1, 2, 3, 4, 5]
        toMove = 3
        arrayExpected = [1, 2, 5, 4, 3]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_8(self):
        initialArray = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        toMove = 5
        arrayExpected = [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_9(self):
        initialArray = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        toMove = 5
        arrayExpected = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

    def test_case_10(self):
        initialArray = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
        toMove = 5
        arrayExpected = [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5]
        self.assertEqual(moveElementToEnd(initialArray, toMove), arrayExpected)

if __name__ == '__main__':
    unittest.main()