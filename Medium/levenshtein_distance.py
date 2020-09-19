import unittest

# O(nm) time | O(m,n) space
def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])
    return edits[-1][-1]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        str1 = "abc"
        str2 = "yabd"
        self.assertEqual(levenshteinDistance(str1, str2), 2)

    def test_case_2(self):
        str1 = ""
        str2 = "yabd"
        self.assertEqual(levenshteinDistance(str1, str2), 4)

    def test_case_3(self):
        str1 = "abcdefghijklmn"
        str2 = "yabd"
        self.assertEqual(levenshteinDistance(str1, str2), 12)

    def test_case_4(self):
        str1 = "manuela"
        str2 = "pepe"
        self.assertEqual(levenshteinDistance(str1, str2), 6)


if __name__ == '__main__':
    unittest.main()