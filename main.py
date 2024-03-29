import sys

graph = [[0, 7, sys.maxsize, 8],
         [sys.maxsize, 0, 5, sys.maxsize],
         [sys.maxsize, sys.maxsize, 0, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0]]

def shortest_path(i, j, k, graph):
    if k < 0:
        return graph[i][j]
    if i == j:
        return 0
    without_k = shortest_path(i, j, k-1, graph)
    with_k = shortest_path(i, k, k-1, graph) + shortest_path(k, j, k-1, graph)
    return min(without_k, with_k)

if __name__ == '__main__':
    n = len(graph)  
    shortest_paths = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            shortest_paths[i][j] = shortest_path(i, j, n-1, graph)

    for row in shortest_paths:
        print(row)
