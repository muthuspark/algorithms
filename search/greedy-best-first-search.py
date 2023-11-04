import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_set = []  # Priority queue to store states based on heuristic value
    heapq.heappush(open_set, (heuristic[start], start))
    visited = set()  # Set to keep track of visited states
    
    while open_set:
        print(open_set, visited)
        # Get the state with the lowest heuristic value
        _, current_state = heapq.heappop(open_set)
        if current_state == goal:
            print(f"Goal found! {current_state}")
            return
        
        if current_state in visited:
            continue
        
        visited.add(current_state)

        for neighbor, _ in graph[current_state]:
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))

    print("Goal not found!")


# Example usage
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 7)],
    'D': [('E', 3)],
    'E': [],
}

# Heuristic values for each state, estimated distance to the goal
# In real-world applications, a more sophisticated heuristic might be used.
heuristic = {
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 0,
}

start_state = 'A'
goal_state = 'E'

greedy_best_first_search(graph, start_state, goal_state, heuristic)
