import itertools
import timeit

# No path 'x' as floating-point infinity. Single character for tidyness. 
x = float('inf')

# Create graph
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

# Start recursive function
def shortestpath(start, end, intermediate, distance):
   
    if intermediate < 0:
        return(distance[start][end])

    # Return the minimum between two paths with a different intermediate end
    return min(shortestpath(start, end, intermediate - 1, distance),
               shortestpath(start, intermediate, intermediate - 1, distance) +
               shortestpath(intermediate, end, intermediate - 1, distance))

def floyd(distance):

    # Calculate the node-path combinations
    for start_node, end_node in itertools.product(range(maxLength),
                                                  range(maxLength)):

        # If start and end are equal then distance is zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Runs the shortest path to calculate the shortest path between
        # start node and end node
        distance[start_node][end_node] = shortestpath(start_node,
                                                      end_node,
                                                      maxLength - 1, distance)
    return distance

if __name__ == '__main__':
    
    # Calls the function floyd and passes the definition of graph
    print("---------------------")
    print("(2) Shortest distances of (1):")
    print(graph)
    print("---------------------")
    print("Performance duration of (1) and (2) in seconds:")
    print (timeit.timeit())


