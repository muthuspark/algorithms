"""
Implementing the B* (B-star) search algorithm can be a bit more complex than A* 
because it requires maintaining both primary and secondary heuristics, as well as balancing the two heuristics during the search. 
Below is a Python program for a simplified version of B* search. 
Keep in mind that the B* algorithm can be more complex in practice and often requires careful consideration of heuristics. 
This example focuses on the concept, but real-world applications may involve additional details and optimizations.
"""
import heapq

def b_star_search(graph, start, goal, primary_heuristic, secondary_heuristic):
    open_set = [(0, start)]  # Priority queue to store (f-cost, state) pairs
    g_costs = {node: float('inf') for node in graph}  # Initialize g-costs to infinity
    g_costs[start] = 0
    visited = set()

    while open_set:
        f_cost, current_state = heapq.heappop(open_set)

        if current_state == goal:
            print("Goal found!")
            return

        if current_state in visited:
            continue

        visited.add(current_state)

        for neighbor, cost in graph[current_state]:
            tentative_g_cost = g_costs[current_state] + cost
            if tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                h_cost = primary_heuristic[neighbor]
                h2_cost = secondary_heuristic[neighbor]
                f_cost = tentative_g_cost + max(h_cost, h2_cost)  # B* balance
                heapq.heappush(open_set, (f_cost, neighbor))

    print("Goal not found!")

# Example usage
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 7)],
    'D': [('E', 3)],
    'E': [],
}

primary_heuristic = {
    'A': 8,  # Primary heuristic values for each state, estimated distance to the goal
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 0,
}

secondary_heuristic = {
    'A': 6,  # Secondary heuristic values for each state
    'B': 4,
    'C': 3,
    'D': 1,
    'E': 0,
}

start_state = 'A'
goal_state = 'E'

b_star_search(graph, start_state, goal_state, primary_heuristic, secondary_heuristic)