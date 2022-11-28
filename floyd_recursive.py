import itertools

# Setup variable for no path as infinity
noPath = float('inf')

# Setup graph input
graph = [[0, 7, noPath, 8],
         [noPath, 0, 5, noPath],
         [noPath, noPath, 0, 2],
         [noPath, noPath, noPath, 0]]

maxLength = len(graph[0])

# Floyd Recursion function
def shortestpath(start, end, intermediate, distance):
    
    # Solve paths direct or intermediate
    if intermediate < 0:
        return(distance[start][end])

    # Find minima
    return min(shortestpath(start, end, intermediate - 1, distance),
               shortestpath(start, intermediate, intermediate - 1, distance) +
               shortestpath(intermediate, end, intermediate - 1, distance))

# Floyd function in itself
def floyd(distance):

    # Go through each pair
    for startNode, endNode in itertools.product(range(maxLength),
                                                  range(maxLength)):

        # Fact that if we are going where we are we are already there and move on
        if startNode == endNode:
            distance[startNode][endNode] = 0
            continue

        # Find shortest distances
        distance[startNode][endNode] = shortestpath(startNode,
                                                      endNode,
                                                      maxLength - 1, distance)
    # Return the shortest distances
    return distance

if __name__ == '__main__':
    print(floyd(graph))
