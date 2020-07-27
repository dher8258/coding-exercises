import unittest

# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
	newLetterCode = alphabet.index(letter) + key
	return alphabet[newLetterCode] if newLetterCode <= 25 else \
			alphabet[newLetterCode % 26]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")

    def test_case_2(self):
        self.assertEqual(caesarCipherEncryptor("abc", 0), "abc")

    def test_case_3(self):
        self.assertEqual(caesarCipherEncryptor("abc", 3), "def")

    def test_case_4(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 5), "cde")

    def test_case_5(self):
        self.assertEqual(caesarCipherEncryptor("abc", 26), "abc")

    def test_case_6(self):
        self.assertEqual(caesarCipherEncryptor("abc", 52), "abc")

    def test_case_7(self):
        self.assertEqual(caesarCipherEncryptor("abc", 57), "fgh")

    def test_case_8(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 25), "wxy")

    def test_case_9(self):
        self.assertEqual(caesarCipherEncryptor("iwufqnkqkqoolxzzlzihqfm", 25), "hvtepmjpjpnnkwyykyhgpel")

    def test_case_10(self):
        self.assertEqual(caesarCipherEncryptor("ovmqkwtujqmfkao", 52), "ovmqkwtujqmfkao")
    
    def test_case_11(self):
        self.assertEqual(caesarCipherEncryptor("mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf", 7), "tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm")

    def test_case_12(self):
        self.assertEqual(caesarCipherEncryptor("kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh", 15), "zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw")

if __name__ == '__main__':
    unittest.main()