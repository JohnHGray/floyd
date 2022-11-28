import unittest
import timeit


from floydRecursive import shortestpath
from floydRecursive import floyd


# Test recursion
class ShortPathTestCase(unittest.TestCase):

    def test_shortpath_function(self):
        x = float('inf')
        graph = [[0, 7, 9, 8, x, 6, x, 5],
                 [1, 0, 5, 6, 4, 3, x, 8],
                 [4, 4, 0, 2, x, 2, 1, 7],
                 [8, x, 3, 0, 3, 7, 2, 4],
                 [1, 3, x, 1, 0, 2, 1, 9],
                 [1, 3, 7, x, 1, 0, x, 6],
                 [1, x, 7, 1, 1, 3, 0, x],
                 [1, 3, 7, 1, x, 6, 3, 0]]
        result = shortestpath(0, 1, 3, graph)
        self.assertEqual(result, 8)

    print("---------------------")
    print("Performance duration in seconds")
    print (timeit.timeit())


# Test function
class FloydOutputTestCase(unittest.TestCase):

    def test_floyd_function(self):
        x = float('inf')
        graph = [[0, 7, 9, 8, x, 6, x, 5],
                 [1, 0, 5, 6, 4, 3, x, 8],
                 [4, 4, 0, 2, x, 2, 1, 7],
                 [8, x, 3, 0, 3, 7, 2, 4],
                 [1, 3, x, 1, 0, 2, 1, 9],
                 [1, 3, 7, x, 1, 0, x, 6],
                 [1, x, 7, 1, 1, 3, 0, x],
                 [1, 3, 7, 1, x, 6, 3, 0]]
        MAX_LENGTH = len(graph[0])
        shortest_graph = [[0, 7, 9, 6, 7, 6, 8, 5],
                 [1, 0, 5, 5, 4, 3, 5, 6],
                 [2, 4, 0, 2, 2, 2, 1, 6],
                 [3, 6, 3, 0, 3, 5, 2, 4],
                 [1, 3, 4, 1, 0, 2, 1, 5],
                 [1, 3, 5, 2, 1, 0, 2, 6],
                 [1, 4, 4, 1, 1, 3, 0, 5],
                 [1, 3, 4, 1, 4, 6, 3, 0]]
        result = floyd(graph)
        self.assertEqual(result, shortest_graph)

   