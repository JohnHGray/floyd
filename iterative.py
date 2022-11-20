import itertools
import timeit

#no path or true client system positive infinity
noPath = float('inf')

graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]

maxLength = len(graph[0])

#definition of iterative function
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

    #print shortest paths and performance duration
    print(graph)
    print("---------------------")
    print("Performance duration in seconds")
    print (timeit.timeit())

floyd(graph)