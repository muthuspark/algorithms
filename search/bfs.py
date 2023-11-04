from collections import deque

class Graph:
    """
    This class represents a graph and provides methods for breadth-first traversal.
    """
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """
        This method adds an edge between two vertices in the graph.
        If the source vertex already exists in the graph, the destination vertex
        is appended to its adjacency list.
        If the source vertex does not exist, a new key-value pair is added to
        the graph dictionary, where the key is the source vertex and the value
        is a list containing the destination vertex.
        """
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        """
        This method performs a breadth-first traversal starting from a given node.
        It prints the visited nodes in the traversal order.
        """
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            print('visiting', node, end='\n')

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth-First Traversal (starting from vertex 2):")
g.bfs(2)