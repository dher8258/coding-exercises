import unittest

# O(n) time | O(n) space
# Where n is the total number of elements in the array
def spiral_traverse(array):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    while start_row <=  end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
			
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
			
        for col in reversed(range(start_col, end_col)):
            # Handle the edge case when there's a single row
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this row, which
            # we've already counted in the first for loop above
            # See Test Case 8 for an example of this edge case.
            if start_row == end_row:
                break
            result.append(array[end_row][col])
		
        for row in reversed(range(start_row + 1, end_row)):
            # Handle the edge case when there's a single column
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this column, which
            # we've already counted in the first for loop above
            # See Test Case 9 for an example of this edge case.
            if start_col == end_col:
                break
            result.append(array[row][start_col])
			
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    
    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_2(self):
        array = [[1]]
        result = [1]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_3(self):
        array = [[1, 2], [4, 3]]
        result = [1, 2, 3, 4]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_4(self):
        array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_5(self):
        array = [
            [19, 32, 33, 34, 25, 8],
            [16, 15, 14, 13, 12, 11],
            [18, 31, 36, 35, 26, 9],
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [17, 30, 29, 28, 27, 10]
            ]
        result = [19,32,33,34,25,8,11,9,6,7,10,27,28,29,30,17,
                20,1,18,16,15,14,13,12,26,5,24,23,22,21,2,31,36,
                35,4,3]
        self.assertEqual(spiral_traverse(array), result)
    
    def test_case_6(self):
        array = [
            [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
            [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
            ]
        result = [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_7(self):
        array = [
            [27, 12, 35, 26],
            [25, 21, 94, 11],
            [19, 96, 43, 56],
            [55, 36, 10, 18],
            [96, 83, 31, 94],
            [93, 11, 90, 16]
            ]
        result = [27,12,35,26,11,56,18,94,16,90,11,93,96,55,19,
                25,21,94,43,10,31,83,36,96]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_8(self):
        array = [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]
        result =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_9(self):
        array = [[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(spiral_traverse(array), result)

    def test_case_10(self):
        array = [
                [1, 11],
                [2, 12],
                [3, 13],
                [4, 14],
                [5, 15],
                [6, 16],
                [7, 17],
                [8, 18],
                [9, 19],
                [10, 20]
                ]
        result = [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.assertEqual(spiral_traverse(array), result)

if __name__ == '__main__':
    unittest.main()