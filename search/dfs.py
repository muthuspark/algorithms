class Graph:
    """
    This class represents a graph and provides methods for depth-first traversal.
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

    def dfs(self, node, visited):
        """
        This method performs a depth-first traversal starting from a given node.
        It prints the visited nodes in the traversal order.
        """
        if node not in visited:
            print('visiting', node, end='\n')
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                self.dfs(neighbor, visited)

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal (starting from vertex 2):")
visited = set()
g.dfs(2, visited)
