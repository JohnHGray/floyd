import itertools
import timeit

# Setup variable for no path as infinity
noPath = float('inf')

# Create square matrix for input
graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]

# Print graph input for later comparison
print("---------------------")
print("(1) Given graph:")
print(graph)

maxLength = len(graph[0])

# Iterative function
def floyd(distance):

    # Loop through each step
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