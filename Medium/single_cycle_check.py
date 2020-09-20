import unittest

"""
Given an array of integers where each integer represents a jump of its value in the array. 
For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3
represents a jump of three indices backwards in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of
-1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in
the array brings us to index 0.

The function returns a boolean representing whether the jumps in the array form a single cycle.
A single cycle occurs if, starting at any index in the array and following the jumps, every element 
in the array is visited exactly once before landing back on the starting index.
"""

# O(n) time | O(1) space
def hasSingleCycle(array):
	numElementsVisited = 0
	currentIdx = 0
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		numElementsVisited += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)


class TestProgramm(unittest.TestCase):
    def test_case_1(self):
        array = [2, 3, 1, -4, -4, 2]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_2(self):
        array = [2, 2, -1]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_3(self):
        array = [2, 2, 2]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_4(self):
        array = [1, 1, 1, 1, 1]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_5(self):
        array = [-1, 2, 2]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_6(self):
        array = [0, 1, 1, 1, 1]
        self.assertEqual(hasSingleCycle(array), False)

    def test_case_7(self):
        array = [1, 1, 0, 1, 1]
        self.assertEqual(hasSingleCycle(array), False)

    def test_case_8(self):
        array = [1, 1, 1, 1, 2]
        self.assertEqual(hasSingleCycle(array), False)

    def test_case_9(self):
        array = [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_10(self):
        array = [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]
        self.assertEqual(hasSingleCycle(array), False)

    def test_case_11(self):
        array = [1, 2, 3, 4, -2, 3, 7, 8, 1]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_12(self):
        array = [1, 2, 3, 4, -2, 3, 7, 8, -8]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_13(self):
        array = [1, 2, 3, 4, -2, 3, 7, 8, -26]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_14(self):
        array = [10, 11, -6, -23, -2, 3, 88, 908, -26]
        self.assertEqual(hasSingleCycle(array), True)

    def test_case_15(self):
        array = [10, 11, -6, -23, -2, 3, 88, 909, -26]
        self.assertEqual(hasSingleCycle(array), False)

    def test_case_16(self):
        array = [1, -1, 1, -1]
        self.assertEqual(hasSingleCycle(array), False)


if __name__ == '__main__':
    unittest.main()