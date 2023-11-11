import queue

dd = []
kk = []
def beam_search(graph, start, goal, beam_width):
    open_set = queue.PriorityQueue()
    open_set.put((0, start))
    closed_set = set()
    
    search_tree = {start: None}  # A dictionary to represent the search tree

    while not open_set.empty():
        dd.append(list(open_set.queue))
        kk.append(list(closed_set))

        current_cost, current_node = open_set.get()
        print(current_node)

        if current_node == goal:
            # Goal reached, reconstruct and return the path
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = search_tree[current_node]
            return path

        closed_set.add(current_node)
        successors = graph[current_node]
        successors.sort(key=lambda x: x[1])  # Sort successors by cost

        for successor, cost in successors[:beam_width]:
            if successor not in closed_set:
                open_set.put((current_cost + cost, successor))
                search_tree[successor] = current_node

    # If goal not reached
    return None

# Example graph represented as an adjacency list with costs
graph = {
    'A': [('E', 4), ('C', 2), ('I', 4)],
    'B': [],
    'C': [('F', 1), ('G', 2), ('H', 8)],
    'D': [('B', 2)],
    'E': [('F', 2), ('C', 2), ('H', 5)],
    'F': [('H', 4), ('G', 1)],
    'G': [('D', 3)],
    'H': [('B', 6)],
    'I': [('H', 3)]
}
start_node = 'A'
goal_node = 'B'
beam_width = 2  # Adjust the beam width as needed

path = beam_search(graph, start_node, goal_node, beam_width)
if path:
    print("Shortest Path:", ' -> '.join(path))
else:
    print("No path found.")

print(dd)
print(kk)
