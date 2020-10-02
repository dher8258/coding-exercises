import unittest

"""
MinMaxStack class for a Min Max Stack. The class supports:
 - Pushing and popping values on and off the stack.
 - Peeking at the value at the top of the stack.
 - Getting both the minimum and the maximum values in the stack at any
 given point in time.

All class methods, when considered independently, run in constant time
with constant space.
"""

class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []
	
	# O(1) time | O(1) space
	def peek(self):
		return self.stack[len(self.stack) - 1]
	
	# O(1) time | O(1) space
	def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()
	
	# O(1) time | O(1) space
	def push(self, number):
		newMinMax = {"min": number, "max": number}
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
			newMinMax["min"] = min(lastMinMax["min"], number)
			newMinMax["max"] = max(lastMinMax["max"], number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)
	
	# O(1) time | O(1) space
	def getMin(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
	
	# O(1) time | O(1) space
	def getMax(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

# Helper method
def testMinMaxPeek(self, min, max, peek, stack):
	self.assertEqual(stack.getMin(), min)
	self.assertEqual(stack.getMax(), max)
	self.assertEqual(stack.peek(), peek)

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		stack = MinMaxStack()
		stack.push(5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		stack.push(7)
		testMinMaxPeek(self, 5, 7, 7, stack)
		stack.push(2)
		testMinMaxPeek(self, 2, 7, 2, stack)
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.pop(), 7)
		testMinMaxPeek(self, 5, 5, 5, stack)

	def test_case_2(self):
		stack = MinMaxStack()
		stack.push(2)
		testMinMaxPeek(self, 2, 2, 2, stack)
		stack.push(7)
		testMinMaxPeek(self, 2, 7, 7, stack)
		stack.push(1)
		testMinMaxPeek(self, 1, 7, 1, stack)
		stack.push(8)
		testMinMaxPeek(self, 1, 8, 8, stack)
		stack.push(3)
		testMinMaxPeek(self, 1, 8, 3, stack)
		stack.push(9)
		testMinMaxPeek(self, 1, 9, 9, stack)
		self.assertEqual(stack.pop(), 9)
		testMinMaxPeek(self, 1, 8, 3, stack)
		self.assertEqual(stack.pop(), 3)
		testMinMaxPeek(self, 1, 8, 8, stack)
		self.assertEqual(stack.pop(), 8)
		testMinMaxPeek(self, 1, 7, 1, stack)
		self.assertEqual(stack.pop(), 1)
		testMinMaxPeek(self, 2, 7, 7, stack)
		self.assertEqual(stack.pop(), 7)
		testMinMaxPeek(self, 2, 2, 2, stack)

	def test_case_3(self):
		stack = MinMaxStack()
		stack.push(5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		stack.push(5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		stack.push(5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		stack.push(5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		stack.push(8)
		testMinMaxPeek(self, 5, 8, 8, stack)
		stack.push(8)
		testMinMaxPeek(self, 5, 8, 8, stack)
		stack.push(0)
		testMinMaxPeek(self, 0, 8, 0, stack)
		stack.push(8)
		testMinMaxPeek(self, 0, 8, 8, stack)
		stack.push(9)
		testMinMaxPeek(self, 0, 9, 9, stack)
		stack.push(5)
		testMinMaxPeek(self, 0, 9, 5, stack)
		self.assertEqual(stack.pop(), 5)
		testMinMaxPeek(self, 0, 9, 9, stack)
		self.assertEqual(stack.pop(), 9)
		testMinMaxPeek(self, 0, 8, 8, stack)
		self.assertEqual(stack.pop(), 8)
		testMinMaxPeek(self, 0, 8, 0, stack)
		self.assertEqual(stack.pop(), 0)
		testMinMaxPeek(self, 5, 8, 8, stack)
		self.assertEqual(stack.pop(), 8)
		testMinMaxPeek(self, 5, 8, 8, stack)
		self.assertEqual(stack.pop(), 8)
		testMinMaxPeek(self, 5, 5, 5, stack)
		self.assertEqual(stack.pop(), 5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		self.assertEqual(stack.pop(), 5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		self.assertEqual(stack.pop(), 5)
		testMinMaxPeek(self, 5, 5, 5, stack)
		self.assertEqual(stack.pop(), 5)

	def test_case_4(self):
		stack = MinMaxStack()
		stack.push(2)
		testMinMaxPeek(self, 2, 2, 2, stack)
		stack.push(0)
		testMinMaxPeek(self, 0, 2, 0, stack)
		stack.push(5)
		testMinMaxPeek(self, 0, 5, 5, stack)
		stack.push(4)
		testMinMaxPeek(self, 0, 5, 4, stack)
		self.assertEqual(stack.pop(), 4)
		testMinMaxPeek(self, 0, 5, 5, stack)
		self.assertEqual(stack.pop(), 5)
		testMinMaxPeek(self, 0, 2, 0, stack)
		stack.push(4)
		testMinMaxPeek(self, 0, 4, 4, stack)
		stack.push(11)
		testMinMaxPeek(self, 0, 11, 11, stack)
		stack.push(-11)
		testMinMaxPeek(self, -11, 11, -11, stack)
		self.assertEqual(stack.pop(), -11)
		testMinMaxPeek(self, 0, 11, 11, stack)
		self.assertEqual(stack.pop(), 11)
		testMinMaxPeek(self, 0, 4, 4, stack)
		self.assertEqual(stack.pop(), 4)
		testMinMaxPeek(self, 0, 2, 0, stack)
		self.assertEqual(stack.pop(), 0)
		testMinMaxPeek(self, 2, 2, 2, stack)
		self.assertEqual(stack.pop(), 2)
		stack.push(6)
		testMinMaxPeek(self, 6, 6, 6, stack)
		self.assertEqual(stack.pop(), 6)


if __name__ == '__main__':
	unittest.main()