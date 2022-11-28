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
def shortestPath(start, end, intermediate, distance):
  
    # Solve paths direct or intermediate
    if intermediate < 0:
        return(distance[start][end])

    # Find minima
    return min(shortestPath(start, end, intermediate - 1, distance),
               shortestPath(start, intermediate, intermediate - 1, distance) +
               shortestPath(intermediate, end, intermediate - 1, distance))

# Floyd function in itself
def floyd(distance):

    # Go through each pair
    for startNode, endNode in itertools.product(range(maxLength),
                                                  range(maxLength)):

        # Fact that if we are going where we are we are already there
        if startNode == endNode:
            distance[startNode][endNode] = 0
            continue

        # find shortest distances
        distance[startNode][endNode] = shortestPath(startNode,
                                                      endNode,
                                                      maxLength - 1, distance)
    # Return the shortest distances
    return distance

if __name__ == '__main__':
    # Recalls function and prints solution
    print(floyd(graph))
