import unittest

class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)

	# O(n) time | O(1) space
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	# O(log(n)) time | O(1) space
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return

	# O(log(n)) time | O(1) space
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

	# O(1) time | O(1) space
	def peek(self):
		return self.heap[0]

	# O(log(n)) time | O(1) space
	def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

	# O(log(n)) time | O(1) space
	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]


# Helper function
def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True


class TestProgramm(unittest.TestCase):
	def test_case_1(self):
		minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
		minHeap.insert(76)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), -5)
		self.assertEqual(minHeap.remove(), -5)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), 2)
		self.assertEqual(minHeap.remove(), 2)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), 6)
		minHeap.insert(87)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_2(self):
		minHeap = MinHeap([2, 3, 1])
		self.assertEqual(minHeap.peek(), 1)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_3(self):
		minHeap = MinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(minHeap.peek(), 1)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_4(self):
		minHeap = MinHeap([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8])
		self.assertEqual(minHeap.peek(), -10)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_5(self):
		minHeap = MinHeap([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])
		self.assertEqual(minHeap.remove(), -10)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), -10)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(-8)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), -10)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -10)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), -9)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(8)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.peek(), -9)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_6(self):
		minHeap = MinHeap([427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212,
    			-484, 603, 934, -848, -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215,
    			564, -710, 710, 565, 892, 970, -755, 55, 821, -3, -153, 240, -160, -610, -583, -27, 131])
		self.assertEqual(minHeap.peek(), -991)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_7(self):
		minHeap = MinHeap([991, -731, -882, 100, 280, -43, 432, 771, -581, 180, -382, -998, 847, 80, -220, 680,
    				769, -75, -817, 366, 956, 749, 471, 228, -435, -269, 652, -331, -387, -657, -255, 382, -216,
    				-6, -163, -681, 980, 913, -169, 972, -523, 354, 747, 805, 382, -827, -796, 372, 753, 519, 906])
		self.assertEqual(minHeap.remove(), -998)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -882)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -827)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(992)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_8(self):
		minHeap = MinHeap([544, -578, 556, 713, -655, -359, -810, -731, 194, -531, -685, 689, -279, -738,
    			886, -54, -320, -500, 738, 445, -401, 993, -753, 329, -396, -924, -975, 376, 748, -356, 972,
    			459, 399, 669, -488, 568, -702, 551, 763, -90, -249, -45, 452, -917, 394, 195, -877, 153,
    			153, 788, 844, 867, 266, -739, 904, -154, -947, 464, 343, -312, 150, -656, 528, 61, 94, -581])
		self.assertEqual(minHeap.peek(), -975)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

	def test_case_9(self):
		minHeap = MinHeap([-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829,
    			59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359,
				238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, 
				-575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 
				157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59])
		minHeap.insert(2)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(22)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(222)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		minHeap.insert(2222)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -987)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -950)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -949)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		self.assertEqual(minHeap.remove(), -942)
		self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
		

if __name__ == '__main__':
	unittest.main()