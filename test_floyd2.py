import unittest

from floyd_recursive import shortestpath
from floyd_recursive import floyd

# Test the recursive function finds shortest intermediate path for pair 0,2 is 12
class test1(unittest.TestCase):

    def testSolution1(self):
        noPath = float('inf')
        graphInput = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestpath(0, 2, 3, graphInput)
        self.assertEqual(result, 12)

# Test the recursive function find shortest intermediate path for pair 1,3 is 7
class test2(unittest.TestCase):

    def testSolution2(self):
        noPath = float('inf')
        graphInput = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestpath(1, 3, 3, graphInput)
        self.assertEqual(result, 7)

# Test the function solution overall
class test3(unittest.TestCase):

    def testSolution3(self):
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