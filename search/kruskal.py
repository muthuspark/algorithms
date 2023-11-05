import numpy as np

class DisjointSet:
    def __init__(self, size):
        
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

def kruskal(graph):
    # Sort edges in ascending order of weight
    edges = sorted(graph, key=lambda edge: edge[2])
    
    # Calculate the number of unique nodes in the graph
    num_nodes = len(np.unique(graph[:, :2]))
    min_spanning_tree = []
    disjoint_set = DisjointSet(num_nodes)
    
    for edge in edges:
        node1, node2, weight = edge
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            min_spanning_tree.append(edge)
            disjoint_set.union(node1, node2)
    
    return min_spanning_tree

# Example usage
graph = np.array([
    (0, 1, 6),
    (0, 3, 8),
    (0, 4, 5),
    (0, 5, 7),
    (1, 2, 4),
    (1, 3, 3),
    (2, 3, 6),
    (3, 4, 4),
    (4, 5, 5)
])
min_spanning_tree = kruskal(graph)
for edge in min_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")