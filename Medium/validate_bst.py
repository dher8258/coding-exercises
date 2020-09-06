import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(d) space, where d is the depth of the tree		
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))
	
def validateBstHelper(tree, minValue, maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        self.assertEqual(validateBst(root), True)

    def test_case_2(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.left = None
        root.right.right = BST(22)
        root.right.right.left = None
        root.right.right.right = None
        root.left.left = BST(2)
        root.left.right = BST(5)
        root.left.right.left = BST(2)
        root.left.right.right = BST(5)
        root.left.right.right.left = None
        root.left.right.right.right = None
        root.left.left.left = BST(1)
        root.left.left.right = None
        root.left.left.left.left = BST(-5)
        root.left.left.left.right = None
        root.left.left.left.left.left = BST(-15)
        root.left.left.left.left.right = BST(-5)
        root.left.left.left.left.right.left = None
        root.left.left.left.left.right.right = BST(-2)
        root.left.left.left.left.right.right.left = None
        root.left.left.left.left.right.right.right = BST(-1)
        root.left.left.left.left.right.right.right.left = None
        root.left.left.left.left.right.right.right.right = None
        root.left.left.left.left.left.left = BST(-22)
        root.left.left.left.left.left.right = None
        root.left.left.left.left.left.left.left = None
        root.left.left.left.left.left.left.right = None
        self.assertEqual(validateBst(root), False)

    def test_case_3(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.left = None
        root.right.right = None
        root.left.left = None
        root.left.right = BST(10)
        root.left.right.left = None
        root.left.right.right = None
        self.assertEqual(validateBst(root), False)


if __name__ == '__main__':
    unittest.main()

