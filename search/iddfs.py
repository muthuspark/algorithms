def depthLimitedDFS(graph, node, goal, depth_limit):
    """
    This method performs a depth-limited depth-first search (DFS) on a graph.
    It starts at the given node and continues until it reaches the goal node or
    until the depth limit is reached.
    If the goal node is found, it returns the node.
    If the depth limit is reached or if there are no more neighbors to explore,
    it returns None.
    """
    if node == goal:
        return node

    if depth_limit <= 0:
        return None

    for neighbor in graph[node]:
        result = depthLimitedDFS(graph, neighbor, goal, depth_limit - 1)
        if result:
            return result

    return None

def iterativeDeepeningDFS(graph, start, goal):
    depth_limit = 0

    while True:
        result = depthLimitedDFS(graph, start, goal, depth_limit)
        if result:
            return result  # Goal found
        depth_limit += 1

        if depth_limit > len(graph):
            break  # Stop if the depth limit exceeds the number of nodes

    return None  # Goal not found

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': ['H', 'I'],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'

result = iterativeDeepeningDFS(graph, start_node, goal_node)

if result:
    print(f"Goal '{goal_node}' found using IDDFS.")
else:
    print(f"Goal '{goal_node}' not found using IDDFS.")
