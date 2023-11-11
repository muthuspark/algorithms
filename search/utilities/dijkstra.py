from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    # Initialize distances dictionary with all vertices set to infinity
    distances = {v:float('inf') for v in range(graph.v)}
    
    # Set the distance of the start_vertex to 0
    distances[start_vertex] = 0
    print("initial distances: ", distances)
    # Create a priority queue to store vertices and their distances
    pq = PriorityQueue()
    # Add the start_vertex to the priority queue with distance 0
    pq.put((0, start_vertex))
    print("initial Priority Queue: ", pq.queue)
    # Continue until the priority queue is empty
    while not pq.empty():
        # Get the vertex with the minimum distance from the priority queue
        (dist, current_vertex) = pq.get()
        
        # Iterate over the neighbors of the current_vertex
        for neighbor in range(graph.v):
            # Check if there is an edge between the current_vertex and the neighbor
            if graph.edges[current_vertex][neighbor] != -1:
                # Calculate the distance from the current_vertex to the neighbor
                distance = graph.edges[current_vertex][neighbor]
                # Check if the neighbor has not been visited
                if neighbor not in graph.visited:
                    # Calculate the new cost to reach the neighbor
                    old_cost = distances[neighbor]
                    new_cost = distances[current_vertex] + distance
                    # Check if the new cost is smaller than the old cost
                    if new_cost < old_cost:
                        # Update the distance of the neighbor in the distances dictionary
                        distances[neighbor] = new_cost
                        # Add the neighbor to the priority queue with the new cost
                        pq.put((new_cost, neighbor))

        print("Current Vertex: ", current_vertex)
        print("     Current Priority Queue: ", pq.queue)
        print("         Distances: ", distances)
        # Mark the current_vertex as visited
        graph.visited.append(current_vertex)
        print("             Visited: ", graph.visited)
        print("\n\n\n")


    # Return the distances dictionary
    return distances

if __name__ == "__main__":
    # Create a sample graph
    g = Graph(9)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 6, 5)
    g.add_edge(1, 6, 10)
    g.add_edge(1, 7, 21)
    g.add_edge(1, 2, 8)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 12)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 13)
    g.add_edge(4, 7, 2)
    g.add_edge(4, 8, 6)
    g.add_edge(5, 8, 11)
    g.add_edge(6, 7, 2)
    g.add_edge(7, 8, 4) 
    

    # Find the shortest distances from node 'A'
    start_node = 0
    shortest_distances = dijkstra(g, start_node)
    print(shortest_distances)
    # Print the results
    for vertex in range(len(shortest_distances)):
        print("Distance from vertex 0 to vertex", vertex, "is", shortest_distances[vertex])