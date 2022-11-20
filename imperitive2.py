import itertools
import math

#no edge is no path or true client system infinity

noPath = 99999

graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]

maxLength = len(graph[0])

def floyd(distance):

    for intermediate, start_node, end_node in itertools.product(range(maxLength), range(maxLength),
                         range(maxLength)):

        # if start_node is equal to end_node
        # then distance equals zero

        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # return minima

        distance[start_node][end_node] = min(
                                            distance[start_node][end_node],
                                            distance[start_node][intermediate] +
                                            distance[intermediate][end_node]
                                            )

    print(distance)
    print(graph)
    print("--------------")
    import timeit
    print("Performance test using timeit:")
    print (timeit.timeit())
    print(graph)
floyd(graph)