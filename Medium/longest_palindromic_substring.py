import unittest

"""
Given a string, returns its longest palindromic substring.

A palindrome is a defined as a string that's written the same forward
and backward. Note that single-character strings are palindromes.

We assume that there will only be one longest palindromic substring.
"""

# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
	currentLongest = [0, 1]
	for i in range(1, len(string)):
		odd = getLongestPalindromeFrom(string, i - 1, i + 1)
		even = getLongestPalindromeFrom(string, i - 1, i)
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
	return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		input = "abaxyzzyxf"
		output = "xyzzyx"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_2(self):
		input = "a"
		output = "a"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_3(self):
		input = "it's highnoon"
		output = "noon"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_4(self):
		input = "noon high it is"
		output = "noon"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_5(self):
		input = "abccbait's highnoon"
		output = "abccba"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_6(self):
		input = "abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"
		output = "zzzzzzzzzzzzzzzzzzzz"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_7(self):
		input = "abcdefgfedcba"
		output = "abcdefgfedcba"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_8(self):
		input = "abcdefghfedcbaa"
		output = "aa"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_9(self):
		input = "abcdefggfedcba"
		output = "abcdefggfedcba"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_10(self):
		input = "zzzzzzz2345abbbba5432zzbbababa"
		output = "zz2345abbbba5432zz"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_11(self):
		input = "z234a5abbbba54a32z"
		output = "5abbbba5"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_12(self):
		input = "z234a5abbba54a32z"
		output = "5abbba5"
		self.assertEqual(longestPalindromicSubstring(input), output)

	def test_case_13(self):
		input = "ab12365456321bb"
		output = "b12365456321b"
		self.assertEqual(longestPalindromicSubstring(input), output)


if __name__ == '__main__':
	unittest.main()