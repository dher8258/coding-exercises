import unittest

# O(nm) time | O(min(m,n)) space
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]


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