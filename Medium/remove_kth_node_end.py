import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())

if __name__ == '__main__':
    unittest.main()