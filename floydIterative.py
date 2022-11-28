import itertools
import timeit

# No path 'x' as floating-point infinity. Single character for tidyness. 
x = float('inf')

# Create square matrix for input
graph = [[0, 7, 9, 8, x, 6, x, 5],
         [1, 0, 5, 6, 4, 3, x, 8],
         [4, 4, 0, 2, x, 2, 1, 7],
         [8, x, 3, 0, 3, 7, 2, 4],
         [1, 3, x, 1, 0, 2, 1, 9],
         [1, 3, 7, x, 1, 0, x, 6],
         [1, x, 7, 1, 1, 3, 0, x],
         [1, 3, 7, 1, x, 6, 3, 0]]

print("---------------------")
print("(1) Given graph:")
print(graph)

maxLength = len(graph[0])

# Iterative function
def floyd(distance):

    # Loop through step
    for start, end, intermediate in itertools.product(range(maxLength), range(maxLength), range(maxLength)):

        # If start is equal to end then
        # distance equals zero and continue
        if start == end:
            distance[start][end] = 0
            continue

        # Calculate the shortest path between
        distance[start][end] = min(distance[start][end],distance[start][intermediate] + distance[intermediate][end])
                                            
    # Print shortest paths and performance duration
    print("---------------------")
    print("(2) Shortest distances of (1):")
    print(graph)
    print("---------------------")
    print("Performance duration of (1) and (2) in seconds:")
    print (timeit.timeit())

floyd(graph)