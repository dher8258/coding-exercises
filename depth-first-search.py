import unittest

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) time | O(V),
    # where V = Vertex and E = Edges in the graph
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

    def test_case_2(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[1].addChild("G")
        graph.children[2].addChild("I").addChild("J")
        graph.children[0].children[0].addChild("K").addChild("H")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "K", "H", "F", "C", "G", "D", "I", "J"])

if __name__ == '__main__':
    unittest.main()