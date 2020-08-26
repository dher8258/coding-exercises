import unittest

# O(n) time | O(1) space
def longest_peak(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue
		
        idx_left = i - 2
        while idx_left >= 0 and array[idx_left] < array[idx_left + 1]:
            idx_left -= 1
	
        idx_right = i + 2
        while idx_right < len(array) and array[idx_right] < array[idx_right - 1]:
            idx_right += 1
			
        current_peak_length = idx_right - idx_left - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        i = idx_right
        
    return longest_peak_length

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected_length = 6
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_2(self):
        array = []
        expected_length = 0
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_3(self):
        array = [1, 3, 2]
        expected_length = 3
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_4(self):
        array = [1, 2, 3, 4, 5, 1]
        expected_length = 6
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_5(self):
        array = [5, 4, 3, 2, 1, 2, 1]
        expected_length = 3
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_6(self):
        array = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
        expected_length = 5
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_7(self):
        array = [5, 4, 3, 2, 1, 2, 10, 12]
        expected_length = 0
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_8(self):
        array = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
        expected_length = 0
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_9(self):
        array = [1, 2, 3, 3, 2, 1]
        expected_length = 0
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_10(self):
        array = [1, 1, 3, 2, 1]
        expected_length = 4
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_11(self):
        array = [1, 2, 3, 2, 1, 1]
        expected_length = 5
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_12(self):
        array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
        expected_length = 9
        self.assertEqual(longest_peak(array), expected_length)

    def test_case_13(self):
        array = [1, 2, 3, 3, 4, 0, 10]
        expected_length = 3
        self.assertEqual(longest_peak(array), expected_length)

if __name__ == '__main__':
    unittest.main()
