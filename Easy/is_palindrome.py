import unittest

# O(n) time | O(1) space 
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(isPalindrome("abcdcba"), True)

    def test_case_2(self):
        self.assertEqual(isPalindrome("a"), True)

    def test_case_3(self):
        self.assertEqual(isPalindrome("ab"), False)

    def test_case_4(self):
        self.assertEqual(isPalindrome("aba"), True)

    def test_case_5(self):
        self.assertEqual(isPalindrome("abb"), False)

    def test_case_6(self):
        self.assertEqual(isPalindrome("abba"), True)

    def test_case_7(self):
        self.assertEqual(isPalindrome("abcdefghhgfedcba"), True)

    def test_case_8(self):
        self.assertEqual(isPalindrome("abcdefghihgfeddcba"), False)

if __name__ == '__main__':
    unittest.main()

    
    




    