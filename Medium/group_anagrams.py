import unittest

"""
The function takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't
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
		pass

if __name__ == '__main__':
	unittest.main()