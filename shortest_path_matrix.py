

def bfs(visited, graph, node, matrix):
    visited.append(node)
    queue.append(node)
    distance = 0
    while queue:
        s = queue.pop(0)
        distance += 1
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                if not matrix[node][neighbour]:
                    matrix[node][neighbour] = distance
                    matrix[neighbour][node] = distance
                queue.append(neighbour)


# Generate a corresponding shortest-path matrix.
def generate_shortest_path_matrix(graph):
    shortest_path_matrix = [[0 for _ in range(8)] for _ in range(8)]
    for node in graph.keys():
        visited = []  # List to keep track of visited nodes.
        bfs(visited, graph, node, shortest_path_matrix)
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
        0: [1, 3],
        1: [0, 2],
        2: [1],
        3: [0, 4, 7],
        4: [3, 5, 6, 7],
        5: [4, 6],
        6: [5, 7],
        7: [3, 4, 6]
    }
    matrix = generate_shortest_path_matrix(G)
    print('\n',
          matrix[0], '\n',
          matrix[1], '\n',
          matrix[2], '\n',
          matrix[3], '\n',
          matrix[4], '\n',
          matrix[5], '\n',
          matrix[6], '\n',
          matrix[7], '\n',)
