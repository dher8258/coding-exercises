import unittest

"""
Given a Node class that has a name and an array of optional children nodes. When put together, nodes form
an acyclic tree-like structure.
The breadth-first search method on the Node class takes in an empty array, traverses the tree using the
breadth-first search approach (specifically navigating the tree from left to right), stores all of the 
nodes' names in the input array, and returns it.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	
	# O(v + e) time | O(v) space, where v is the number of vertices of 
	# the input graph and e is the number of edges of the input graph
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    def test_case_2(self):
        graph = Node("A")
        graph.addChild("B").addChild("C")
        graph.children[0].addChild("D")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D"])

    def test_case_3(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D").addChild("E")
        graph.children[1].addChild("F")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F"])

    def test_case_4(self):
        graph = Node("A")
        graph.addChild("B")
        graph.children[0].addChild("C")
        graph.children[0].children[0].addChild("D").addChild("E")
        graph.children[0].children[0].children[0].addChild("F")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F"])

    def test_case_5(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D").addChild("E").addChild("F")
        graph.children[0].addChild("G").addChild("H").addChild("I")
        graph.children[0].children[1].addChild("O").addChild("P").addChild("Q").addChild("R")
        graph.children[0].children[1].children[1].addChild("T").addChild("U")
        graph.children[0].children[1].children[3].addChild("V")
        graph.children[0].children[1].children[3].children[0].addChild("W").addChild("X").addChild("Y")
        graph.children[0].children[1].children[3].children[0].children[1].addChild("Z")
        graph.children[1].addChild("J")
        graph.children[2].addChild("K").addChild("L")
        graph.children[2].children[0].addChild("S")
        graph.children[4].addChild("M").addChild("N")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])


if __name__ == '__main__':
    unittest.main()