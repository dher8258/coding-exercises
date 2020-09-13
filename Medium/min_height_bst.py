import unittest

# O(n) time | O(n) space, where 'n' is the length of the array
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst(array):
	return constructMinHeightBst(array, 0, len(array)  - 1)
	
def constructMinHeightBst(array, startIdx, endIdx):
	if endIdx < startIdx:
		return None
	
	midIdx = (startIdx + endIdx) // 2
	bst = BST(array[midIdx])
	bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
	bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
	return bst


# --- Helper functions for testing
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)

# --- Unit tests
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBst(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])
        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])

# --- Main
if __name__ == '__main__':
    unittest.main()