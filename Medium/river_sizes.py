import unittest

"""
Given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land, and each 1 represent part of a river. A river consists of any number of 1s that are
either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming
a river determine its size.

A river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal 
line; it can be L-shaped, for example.

The function returns an array of the sizes of all rivers represented in the input matrix. The sizes don't
need to be in any particular order.
"""

# O(wh) time | O(wh) space
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
	currentRiverSize = 0
	nodesToExplore = [[i, j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)
			
			
def getUnvisitedNeighbors(i, j, matrix, visited):
	unvisitedNeighbors = []
	if i > 0 and not visited[i - 1][j]:
		unvisitedNeighbors.append([i - 1, j])
	if i < len(matrix) - 1 and not visited[i + 1][j]:
		unvisitedNeighbors.append([i + 1, j])
	if j > 0 and not visited[i][j - 1]:
		unvisitedNeighbors.append([i, j - 1])
	if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
		unvisitedNeighbors.append([i, j + 1])
	return unvisitedNeighbors

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_2(self):
        testInput = [[0]]
        expected = []
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_3(self):
        testInput = [[1]]
        expected = [1]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_4(self):
        testInput = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
        expected = [1, 2, 3]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_5(self):
        testInput = [
            [1, 0, 0, 1], 
            [1, 0, 1, 0], 
            [0, 0, 1, 0], 
            [1, 0, 1, 0]
            ]
        expected = [1, 1, 2, 3]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_6(self):
        testInput = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0], 
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1], 
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], 
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
            ]
        expected = [1, 1, 2, 2, 5, 21]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_7(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1], 
            [0, 1, 0, 0, 0, 1, 0], 
            [0, 0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0], 
            [0, 1, 0, 0, 0, 1, 0], 
            [1, 0, 0, 0, 0, 0, 1]
            ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_8(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1]
            ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 7]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_9(self):
        testInput = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
            ]
        expected = []
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_9(self):
        testInput = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
            ]
        expected = [49]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_10(self):
        testInput = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
            ]
        expected = [49]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_11(self):
        testInput = [
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 1, 1]
            ]
        expected = [3, 5, 6]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_12(self):
        testInput = [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 1]
            ]
        expected = [1, 1, 2, 6, 10]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

if __name__ == '__main__':
    unittest.main()