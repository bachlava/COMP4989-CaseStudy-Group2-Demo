# BFS always finds the shortest path between source and visited nodes
def bfs(visited, graph, node, matrix):
    visited.append(node)
    queue.append(node)
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbour in graph[current_node][0]:
            graph[neighbour][1] = graph[current_node][1] + 1
            if neighbour not in visited:
                visited.append(neighbour)
                if not matrix[node][neighbour]:
                    matrix[node][neighbour] = graph[neighbour][1]
                    matrix[neighbour][node] = graph[neighbour][1]
                queue.append(neighbour)


# Generate a corresponding shortest-path matrix.
def generate_shortest_path_matrix(graph):
    shortest_path_matrix = [[0 for _ in range(8)] for _ in range(8)]
    for node in graph.keys():
        visited = []  # List to keep track of visited nodes.
        bfs(visited, graph, node, shortest_path_matrix)
        print(f'\nBFS from node {node}:')
        for value in graph.values():
            value[1] = 0    # Reset each node's distance counter
    return shortest_path_matrix


if __name__ == "__main__":
    # Given the following graph representing genetic interactions:
    # 1---0   7---6
    # |   | / | / |
    # 2   3---4---5
    # adjacency_matrix = [
    #     # 0  1  2  3  4  5  6  7
    #     [0, 1, 0, 1, 0, 0, 0, 0],  # 0
    #     [1, 0, 1, 0, 0, 0, 0, 0],  # 1
    #     [0, 1, 0, 0, 0, 0, 0, 0],  # 2
    #     [1, 0, 0, 0, 1, 0, 0, 1],  # 3
    #     [0, 0, 0, 1, 0, 1, 1, 1],  # 4
    #     [0, 0, 0, 0, 1, 0, 1, 0],  # 5
    #     [0, 0, 0, 0, 1, 1, 0, 1],  # 6
    #     [0, 0, 0, 1, 1, 0, 1, 0],  # 7
    # ]
    queue = []  # Initialize a queue
    G = {
        0: [[1, 3], 0],
        1: [[0, 2], 0],
        2: [[1], 0],
        3: [[0, 4, 7], 0],
        4: [[3, 5, 6, 7], 0],
        5: [[4, 6], 0],
        6: [[5, 7], 0],
        7: [[3, 4, 6], 0]
    }
    result_matrix = generate_shortest_path_matrix(G)
    print('\n', result_matrix[0], '\n',
          result_matrix[1], '\n',
          result_matrix[2], '\n',
          result_matrix[3], '\n',
          result_matrix[4], '\n',
          result_matrix[5], '\n',
          result_matrix[6], '\n',
          result_matrix[7], '\n',)
