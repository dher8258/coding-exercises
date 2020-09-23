import unittest

"""
Given three inputs, all of which are instances of an AncestralTree class that have an
ancestor property pointing to their youngest ancestor. The first input is the top ancestor
in an ancestral tree (i.e., the only instance that has no ancestor -- its ancestor property
points to None / Null), and the other two inputs are descendants in the ancestral tree.

The function returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor. So in the simple ancestral tree below,
the youngest common ancestor to nodes A and B is node A.

    A
   /
  B
"""

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self

# Helper function
def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees

# O(d) time | O(1) space - where d is depth (height) of the ancestral tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo:
		return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		descendant = descendant.ancestor
		depth += 1
	return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    
    return lowerDescendant


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])

    def test_case_2(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["A"], trees["B"])
        self.assertTrue(yca == trees["A"])

    def test_case_3(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["B"], trees["F"])
        self.assertTrue(yca == trees["A"])

    def test_case_4(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["G"], trees["M"])
        self.assertTrue(yca == trees["A"])

    def test_case_5(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["U"], trees["S"])
        self.assertTrue(yca == trees["A"])

    def test_case_6(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["Z"], trees["M"])
        self.assertTrue(yca == trees["A"])

    def test_case_7(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["O"], trees["I"])
        self.assertTrue(yca == trees["B"])

    def test_case_8(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["T"], trees["Z"])
        self.assertTrue(yca == trees["H"])

    def test_case_9(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["T"], trees["V"])
        self.assertTrue(yca == trees["H"])

    def test_case_10(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["T"], trees["H"])
        self.assertTrue(yca == trees["H"])

    def test_case_11(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["W"], trees["V"])
        self.assertTrue(yca == trees["V"])

    def test_case_12(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["Z"], trees["B"])
        self.assertTrue(yca == trees["B"])

    def test_case_13(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["Q"], trees["W"])
        self.assertTrue(yca == trees["H"])

    def test_case_14(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"], trees["D"], trees["E"], trees["F"])
        trees["B"].addDescendants(trees["G"], trees["H"], trees["I"])
        trees["C"].addDescendants(trees["J"])
        trees["D"].addDescendants(trees["K"], trees["L"])
        trees["F"].addDescendants(trees["M"], trees["N"])
        trees["H"].addDescendants(trees["O"], trees["P"], trees["Q"], trees["R"])
        trees["K"].addDescendants(trees["S"])
        trees["P"].addDescendants(trees["T"], trees["U"])
        trees["R"].addDescendants(trees["V"])
        trees["V"].addDescendants(trees["W"], trees["X"], trees["Y"])
        trees["X"].addDescendants(trees["Z"])

        yca = getYoungestCommonAncestor(trees["A"], trees["A"], trees["Z"])
        self.assertTrue(yca == trees["A"])


if __name__ == '__main__':
    unittest.main()