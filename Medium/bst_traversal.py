import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)
        root.left.left = BST(2)
        root.left.right = BST(5)
        root.left.left.left = BST(1)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)

    def test_case_2(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)
        root.left.left = BST(2)
        root.left.right = BST(5)
        root.left.left.left = BST(1)
        root.left.left.left.left = BST(-5)
        root.left.left.left.left.left = BST(-15)
        root.left.left.left.left.right = BST(-5)
        root.left.left.left.left.right.right = BST(-2)
        root.left.left.left.left.right.right.right = BST(-1)
        root.left.left.left.left.left.left = BST(-22)

        inOrder = [-22, -15, -5, -5, -2, -1, 1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, -5, -15, -22, -5, -2, -1, 5, 15, 22]
        postOrder = [-22, -15, -1, -2, -5, -5, 1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)

    def test_case_3(self):
        root = BST(10)

        inOrder = [10]
        preOrder = [10]
        postOrder = [10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)

    def test_case_4(self):
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)
        root.right.right.right = BST(500)
        root.right.right.right.left = BST(50)
        root.right.right.right.right = BST(1500)
        root.right.right.right.right.right = BST(10000)
        root.right.right.right.right.right.left = BST(2200)
        root.right.right.right.left.right = BST(200)
        root.left.left = BST(2)
        root.left.right = BST(5)
        root.left.left.left = BST(1)

        inOrder = [1, 2, 5, 5, 10, 15, 22, 50, 200, 500, 1500, 2200, 10000]
        preOrder = [10, 5, 2, 1, 5, 15, 22, 500, 50, 200, 1500, 10000, 2200]
        postOrder = [1, 2, 5, 5, 200, 50, 2200, 10000, 1500, 500, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)


if __name__ == '__main__':
    unittest.main()