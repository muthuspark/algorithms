class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_solution(self, dist, parent, src):
        print("Vertex\tDistance from Source\tPath")
        for i in range(self.V):
            path = self.get_path(parent, i, src)
            print(f"{i}\t{dist[i]}\t\t\t{path}")

    def bellman_ford(self, src):
        # Initialize distances and predecessors
        dist = [float('inf')] * self.V
        dist[src] = 0
        parent = [-1] * self.V

        # Relaxation step (V-1 times)
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                print(f"{dist[u]} != {float('inf')} and {dist[u]} + {w} < {dist[v]}")
                self.print_solution(dist, parent, src)
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u

        # Negative cycle detection
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return

        # Print the shortest distances and paths
        self.print_solution(dist, parent, src)

    def get_path(self, parent, v, src):
        path = []
        while v != -1:
            path.insert(0, str(v))
            v = parent[v]
        return " -> ".join(path)


graph = Graph(6)
graph.add_edge(0, 1, 20)
graph.add_edge(0, 5, 10)
graph.add_edge(1, 2, 33)
graph.add_edge(1, 4, 20)
graph.add_edge(2, 3, 1)
graph.add_edge(4, 2, -20)
graph.add_edge(4, 3, -2)
graph.add_edge(5, 4, 50)
graph.add_edge(5, 2, 10)

source_vertex = 0
graph.bellman_ford(source_vertex)
