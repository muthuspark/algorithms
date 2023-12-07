import heapq


def prim(graph):
    # Initialize an empty list to store the minimum spanning tree
    min_spanning_tree = []

    # Initialize a set to keep track of visited vertices
    visited = set()

    # Get the first vertex in the graph as the starting vertex
    start_vertex = list(graph.keys())[0]

    # Create a priority queue to store (weight, vertex, parent) tuples
    priority_queue = [(0, start_vertex, None)]

    # Iterate while the priority queue is not empty
    while priority_queue:
        print(priority_queue)
        # Pop the vertex with the minimum weight from the priority queue
        weight, current_vertex, parent = heapq.heappop(priority_queue)

        # Check if the current vertex has not been visited
        if current_vertex not in visited:
            # Mark the current vertex as visited
            visited.add(current_vertex)

            # If the current vertex has a parent, add the edge 
            # to the minimum spanning tree
            if parent is not None:
                print(parent, current_vertex, weight)
                min_spanning_tree.append((parent, current_vertex, weight))

            # Iterate over the neighbors of the current vertex
            for neighbor, neighbor_weight in graph[current_vertex]:
                # Check if the neighbor has not been visited
                if neighbor not in visited:
                    # Add the neighbor to the priority queue with 
                    # its weight and parent
                    heapq.heappush(
                        priority_queue, (neighbor_weight,
                                         neighbor, current_vertex)
                    )
    return min_spanning_tree


# Example usage
graph = {
    "A": [("B", 6), ("D", 8), ("E", 5), ("F", 7)],
    "B": [("C", 4), ("D", 3), ("A", 6)],
    "C": [("D", 2), ("B", 4)],
    "D": [("B", 3), ("C", 6), ("A", 8), ("E", 4)],
    "E": [("D", 4), ("A", 5), ("F", 5)],
    "F": [("A", 7), ("E", 5)],
}

min_spanning_tree = prim(graph)
for edge in min_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
