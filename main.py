import sys
def floyd_recursive(distance, intermediate=-1, start_node=0, end_node=0, MAX_LENGTH=None):
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Initialize MAX_LENGTH on the first call
    if MAX_LENGTH is None:
        MAX_LENGTH = len(distance)

    # Base case for recursion
    if intermediate == MAX_LENGTH:
        return

    # Recursive case for updating distances
    if intermediate == -1:
        # After considering all intermediates, move to the next pair of nodes
        if end_node == MAX_LENGTH - 1:
            if start_node == MAX_LENGTH - 2:
                # All node pairs have been considered, start the process for intermediates
                floyd_recursive(distance, 0, 0, 0, MAX_LENGTH)
            else:
                # Move to the next start node, reset end node
                floyd_recursive(distance, -1, start_node + 1, 0, MAX_LENGTH)
        else:
            if start_node != end_node:
                # Update the distance for the current pair (start_node, end_node)
                distance[start_node][end_node] = min(distance[start_node][end_node], 
                                                      distance[start_node][intermediate] + distance[intermediate][end_node])
            # Move to the next end node
            floyd_recursive(distance, -1, start_node, end_node + 1, MAX_LENGTH)
    else:
        # Update distances considering the current intermediate
        floyd_recursive(distance, -1, start_node, end_node, MAX_LENGTH)
        # Move to the next intermediate node
        floyd_recursive(distance, intermediate + 1, 0, 0, MAX_LENGTH)

# Example usage
if __name__ == "__main__":
    # Example distance matrix
    graph = [[0, sys.maxsize, -2, sys.maxsize],
             [4, 0, 3, sys.maxsize],
             [sys.maxsize, sys.maxsize, 0, 2],
             [sys.maxsize, -1, sys.maxsize, 0]]
    floyd_recursive(graph)
    print(graph)
