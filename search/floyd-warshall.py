def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize the distance matrix with the graph's adjacency matrix
    distance = [row[:] for row in graph]
    print(distance)
    # Loop through all vertices as intermediate nodes
    for k in range(n):
        # Pick all vertices as source one by one
        for i in range(n):
            # Pick all vertices as destination for the above source
            for j in range(n):
                # If the new path through k is shorter, update the distance
                print(f"i={i}, j={j}, k={k} {distance[i][k]} + {distance[k][j]} < {distance[i][j]}")
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
        print(f"distance = {distance}")

    return distance

# Example adjacency matrix for a graph with 4 nodes (0, 1, 2, 3)
INF = float('inf')
graph = [
    [0, 5, 9, 3],
    [2, 0, 4, INF],
    [INF, INF, 0, 3],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)