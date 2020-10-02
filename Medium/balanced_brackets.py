import unittest

"""
The function takes in a string made up of brackets (, [. {, },], and )
and other optional characters. The function returns a boolean representing
whether the string is balanced with regards to brackets.

A string is said to be balanced if it has as many opening brackets of a
certain type as it has closing brackets of that type and if no bracket is
unmatched. Note that an opening bracket can't match a corresponding closing
bracket that comes before it, and similarly, a closing bracket can't match
a corresponding opening bracket that comes after it. Also, brackets can't
overlap each other as in [(]).
"""

# O(n) time | O(n) space
def balancedBrackets(string):
	openingBrackets = "([{"
	closingBrackets = ")]}"
	matchingBrackets = {")": "(", "]": "[", "}": "{"}
	stack = []
	for char in string:
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(balancedBrackets("([])(){}(())()()"), True)

	def test_case_2(self):
		self.assertEqual(balancedBrackets("()[]{}{"), False)

	def test_case_3(self):
		self.assertEqual(balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"), False)

	def test_case_4(self):
		self.assertEqual(balancedBrackets("()()[{()})]"), False)

	def test_case_5(self):
		self.assertEqual(balancedBrackets("(()())((()()()))"), True)

	def test_case_6(self):
		self.assertEqual(balancedBrackets("{}()"), True)

	def test_case_7(self):
		self.assertEqual(balancedBrackets("()([])"), True)

	def test_case_8(self):
		self.assertEqual(balancedBrackets("((){{{{[]}}}})"), True)

	def test_case_9(self):
		self.assertEqual(balancedBrackets("((({})()))"), True)

	def test_case_10(self):
		self.assertEqual(balancedBrackets("(([]()()){})"), True)

	def test_case_11(self):
		self.assertEqual(balancedBrackets("(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())"), True)

	def test_case_12(self):
		self.assertEqual(balancedBrackets("{[[[[({(}))]]]]}"), False)

	def test_case_13(self):
		self.assertEqual(balancedBrackets("[((([])([]){}){}){}([])[]((())"), False)

	def test_case_14(self):
		self.assertEqual(balancedBrackets(")[]}"), False)

	def test_case_15(self):
		self.assertEqual(balancedBrackets("(a)"), True)

	def test_case_16(self):
		self.assertEqual(balancedBrackets("(a("), False)


if __name__ == "__main__":
	unittest.main()