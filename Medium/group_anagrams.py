import unittest

"""
The function takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter.
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo"
are anagrams.

The function returns a list of anagram groups in no particular order.

Sample Input:
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output:
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""

# O(w * n * log(n)) time | O(w * n) space - where w is the number of words
# n is the length of the longest word
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
		expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
		output = list(map(lambda x: sorted(x), groupAnagrams(words)))

		self.compare(expected, output)

	def test_case_2(self):
		words = ["melon", "avion", "hola", "zouk", "kouz", "loah", "onavi", "onmel", "lemon", "aloh"]
		expected = [["melon", "lemon", "onmel"], ["avion", "onavi"], ["aloh", "hola", "loah"], ["kouz", "zouk"]]
		output = list(map(lambda x: sorted(x), groupAnagrams(words)))

		self.compare(expected, output)

	def compare(self, expected, output):
		if len(expected) == 0:
			self.assertEqual(output, expected)
			return
		self.assertEqual(len(expected), len(output))
		for group in expected:
			self.assertTrue(sorted(group) in output)

if __name__ == '__main__':
	unittest.main()