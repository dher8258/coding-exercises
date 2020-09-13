import unittest

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self


def invertBinaryTree(tree):
	if tree is None:
		return
	swapLeftAndRight(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left
		
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
        invertBinaryTree(tree)
        self.assertTrue(tree.__eq__(invertedTree))

    def test_case_2(self):
        tree = BinaryTree(1)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left, None)
        self.assertEqual(tree.right, None)

    def test_case_3(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left, None)
        self.assertEqual(tree.right.right, None)

    def test_case_4(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left, None)
        self.assertEqual(tree.left.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left, None)
        self.assertEqual(tree.right.right, None)

    def test_case_5(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.right = BinaryTree(3)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left, None)
        self.assertEqual(tree.left.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left, None)
        self.assertEqual(tree.right.right.right, None)

    def test_case_6(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right = BinaryTree(3)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left, None)
        self.assertEqual(tree.left.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left, None)
        self.assertEqual(tree.right.right.right, None)

    def test_case_7(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right = BinaryTree(3)
        tree.right.left = BinaryTree(6)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left, None)
        self.assertEqual(tree.left.right.value, 6)
        self.assertEqual(tree.left.right.left, None)
        self.assertEqual(tree.left.right.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left, None)
        self.assertEqual(tree.right.right.right, None)

    def test_case_8(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right = BinaryTree(3)
        tree.right.left = BinaryTree(6)
        tree.right.right = BinaryTree(7)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left.value, 7)
        self.assertEqual(tree.left.left.left, None)
        self.assertEqual(tree.left.left.right, None)
        self.assertEqual(tree.left.right.value, 6)
        self.assertEqual(tree.left.right.left, None)
        self.assertEqual(tree.left.right.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left, None)
        self.assertEqual(tree.right.right.right, None)

    def test_case_9(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.left.left = BinaryTree(8)
        tree.left.right = BinaryTree(5)
        tree.right = BinaryTree(3)
        tree.right.left = BinaryTree(6)
        tree.right.right = BinaryTree(7)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left.value, 7)
        self.assertEqual(tree.left.left.left, None)
        self.assertEqual(tree.left.left.right, None)
        self.assertEqual(tree.left.right.value, 6)
        self.assertEqual(tree.left.right.left, None)
        self.assertEqual(tree.left.right.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left, None)
        self.assertEqual(tree.right.right.right.value, 8)
        self.assertEqual(tree.right.right.right.left, None)
        self.assertEqual(tree.right.right.right.right, None)

    def test_case_10(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.left.left = BinaryTree(8)
        tree.left.left.right = BinaryTree(9)
        tree.left.right = BinaryTree(5)
        tree.left.right.left = BinaryTree(10)
        tree.right = BinaryTree(3)
        tree.right.left = BinaryTree(6)
        tree.right.right = BinaryTree(7)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left.value, 7)
        self.assertEqual(tree.left.left.left, None)
        self.assertEqual(tree.left.left.right, None)
        self.assertEqual(tree.left.right.value, 6)
        self.assertEqual(tree.left.right.left, None)
        self.assertEqual(tree.left.right.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right.value, 10)
        self.assertEqual(tree.right.left.right.left, None)
        self.assertEqual(tree.right.left.right.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left.value, 9)
        self.assertEqual(tree.right.right.left.left, None)
        self.assertEqual(tree.right.right.left.right, None)
        self.assertEqual(tree.right.right.right.value, 8)
        self.assertEqual(tree.right.right.right.left, None)
        self.assertEqual(tree.right.right.right.right, None)

    def test_case_11(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.left.left = BinaryTree(8)
        tree.left.left.left.right = BinaryTree(12)
        tree.left.left.right = BinaryTree(9)
        tree.left.left.right.left = BinaryTree(13)
        tree.left.left.right.right = BinaryTree(14)
        tree.left.right = BinaryTree(5)
        tree.left.right.left = BinaryTree(10)
        tree.right = BinaryTree(3)
        tree.right.left = BinaryTree(6)
        tree.right.left.right = BinaryTree(11)
        tree.right.left.right.left = BinaryTree(15)
        tree.right.left.right.left.right = BinaryTree(17)
        tree.right.left.right.left.right.right = BinaryTree(18)
        tree.right.left.right.left.right.right.right = BinaryTree(19)
        tree.right.left.right.left.right.right.right.left = BinaryTree(20)
        tree.right.left.right.left.right.right.right.left.left = BinaryTree(21)
        tree.right.left.right.right = BinaryTree(16)
        tree.right.right = BinaryTree(7)
        invertBinaryTree(tree)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.left.left.value, 7)
        self.assertEqual(tree.left.left.left, None)
        self.assertEqual(tree.left.left.right, None)
        self.assertEqual(tree.left.right.value, 6)
        self.assertEqual(tree.left.right.left.value, 11)
        self.assertEqual(tree.left.right.left.left.value, 16)
        self.assertEqual(tree.left.right.left.left.left, None)
        self.assertEqual(tree.left.right.left.left.right, None)
        self.assertEqual(tree.left.right.left.right.value, 15)
        self.assertEqual(tree.left.right.left.right.left.value, 17)
        self.assertEqual(tree.left.right.left.right.left.left.value, 18)
        self.assertEqual(tree.left.right.left.right.left.left.left.value, 19)
        self.assertEqual(tree.left.right.left.right.left.left.left.left, None)
        self.assertEqual(tree.left.right.left.right.left.left.left.right.value, 20)
        self.assertEqual(tree.left.right.left.right.left.left.left.right.left, None)
        self.assertEqual(tree.left.right.left.right.left.left.left.right.right.value, 21)
        self.assertEqual(tree.left.right.left.right.left.left.left.right.right.left, None)
        self.assertEqual(tree.left.right.left.right.left.left.left.right.right.right, None)
        self.assertEqual(tree.left.right.left.right.left.left.right, None)
        self.assertEqual(tree.left.right.left.right.left.right, None)
        self.assertEqual(tree.left.right.left.right.right, None)
        self.assertEqual(tree.left.right.right, None)
        self.assertEqual(tree.right.value, 2)
        self.assertEqual(tree.right.left.value, 5)
        self.assertEqual(tree.right.left.left, None)
        self.assertEqual(tree.right.left.right.value, 10)
        self.assertEqual(tree.right.left.right.left, None)
        self.assertEqual(tree.right.left.right.right, None)
        self.assertEqual(tree.right.right.value, 4)
        self.assertEqual(tree.right.right.left.value, 9)
        self.assertEqual(tree.right.right.left.left.value, 14)
        self.assertEqual(tree.right.right.left.left.left, None)
        self.assertEqual(tree.right.right.left.left.right, None)
        self.assertEqual(tree.right.right.left.right.value, 13)
        self.assertEqual(tree.right.right.left.right.left, None)
        self.assertEqual(tree.right.right.left.right.right, None)
        self.assertEqual(tree.right.right.right.value, 8)
        self.assertEqual(tree.right.right.right.left.value, 12)
        self.assertEqual(tree.right.right.right.left.left, None)
        self.assertEqual(tree.right.right.right.left.right, None)
        self.assertEqual(tree.right.right.right.right, None)


if __name__ == '__main__':
    unittest.main()