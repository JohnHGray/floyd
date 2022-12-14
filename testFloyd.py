import unittest

# Call in recursive shortestPath floyd functions
from floydRecursive import shortestPath
from floydRecursive import floyd

# Test the shortest path solution for pair [0,2] is 12
class test1(unittest.TestCase):

    def testSubProblem1(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestPath(0, 2, 3, graph)
        self.assertEqual(result, 12)

# Test the shortest path solution for pair [1,3] is 7
class test2(unittest.TestCase):

    def testSubProblem2(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        result = shortestPath(1, 3, 3, graph)
        self.assertEqual(result, 7)

# Test the floyd function solution overall for all pairs
class test3(unittest.TestCase):

    def testSolution(self):
        noPath = float('inf')
        graph = [[0, 7, noPath, 8],
                 [noPath, 0, 5, noPath],
                 [noPath, noPath, 0, 2],
                 [noPath, noPath, noPath, 0]]
        
        graphSolution = [[0, 7, 12, 8],
                         [noPath, 0, 5, 7],
                         [noPath, noPath, 0, 2],
                         [noPath, noPath, noPath, 0]]
        result = floyd(graph)
        self.assertEqual(result, graphSolution)
        print('Graph Solution')
        print(graphSolution)

if __name__ == '__main__':
    unittest.main()