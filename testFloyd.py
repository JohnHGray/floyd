import unittest

# Call in shortestPath and floyd functions
from floydRecursive import shortestPath
from floydRecursive import floyd

# Test the recursive function solve shortest intermediate path for pair 0,2 as 12
class test1(unittest.TestCase):

    def testSubProblem1(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestPath(0, 2, 3, graph)
        self.assertEqual(result, 12)

# Test the recursive function solves shortest intermediate path for pair 1,3 as 7
class test2(unittest.TestCase):

    def testSubProblem2(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestPath(1, 3, 3, graph)
        self.assertEqual(result, 7)

# Test the function solution overall
class test3(unittest.TestCase):

    def testSolution(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        maxLength = len(graph[0])
        graphSolution = [[0, 7, 12, 8],
                         [noPath, 0, 5, 7],
                         [noPath, noPath, 0, 2],
                         [noPath, noPath, noPath, 0]]
        result = floyd(graph)
        self.assertEqual(result, graphSolution)

if __name__ == '__main__':
    unittest.main()