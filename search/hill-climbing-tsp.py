import numpy as np

# Function to create an adjacency matrix based 
# on Euclidean distances between points
def adjacency_matrix(coordinate):
    matrix = np.zeros((len(coordinate), len(coordinate)))

    # Loop through each point
    for i in range(len(coordinate)):
        for j in range(i + 1, len(coordinate)):
            # Calculate Euclidean distance between 
            # points i and j
            p = np.linalg.norm(
                coordinate[i] - coordinate[j])
            # Set distance in both positions of the matrix 
            # (symmetric for undirected graph)
            matrix[i][j] = p
            matrix[j][i] = p
    return matrix

# Function to generate a random solution 
# (permutation of indices)
def solution(matrix):
    return np.random.permutation(len(matrix))

# Calculate total distance of the path in a solution
def total_distance_of_path(matrix, solution):
    return sum(matrix[solution[i]][solution[i - 1]] 
               for i in range(len(solution)))

# Generate neighboring solutions by swapping cities
def get_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            # Swap positions i and j
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors

# Find the best neighbor based on the total 
# distance of the path
def best_neighbors(matrix, solution):
    neighbors = get_neighbors(solution)
    best_neighbour = neighbors[0]
    best_route_length = total_distance_of_path(matrix, 
                                               best_neighbour)
    for neighbour in neighbors:
        current_route_length = total_distance_of_path(matrix, 
                                                      neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length

# Hill Climbing algorithm to find the shortest path
def hill_climbing(coordinate):
    distance_matrix = adjacency_matrix(coordinate)
    current_solution = solution(distance_matrix)
    current_distance = total_distance_of_path(distance_matrix, 
                                                current_solution)
    best_neighbor, best_neighbor_path = best_neighbors(
        distance_matrix, current_solution)
    
    # Continue until the best neighbor has a 
    # longer path than the current solution
    while best_neighbor_path < current_distance:
        current_solution = best_neighbor
        current_distance = best_neighbor_path
        print(current_distance)
        best_neighbor, best_neighbor_path = best_neighbors(
            distance_matrix, current_solution)
    
    return current_distance, current_solution

# coordinate of the points/cities
coordinate = np.array([[50, 98], [54, 6], [34, 66], [63, 52], 
                        [39, 62], [46, 75], [28, 65], [18, 37], 
                        [18, 97], [13, 80]])

# Run the hill climbing algorithm
final_solution = hill_climbing(coordinate)
print(f"Best path: {final_solution[1]}, Distance: {final_solution[0]}")


# coordinate of the points/cities
# coordinate = np.array([
#         [565, 575], [25, 185], [345, 750], [945, 685], [845, 655],
#         [880, 660], [25, 230], [525, 1000], [580, 1175], [650, 1130],
#         [1605, 620], [1220, 580], [1465, 200], [1530, 5], [845, 680],
#         [725, 370], [145, 665], [415, 635], [510, 875], [560, 365], [300, 465],
#         [520, 585], [480, 415], [835, 625], [975, 580], [1215, 245], [1320, 315],
#         [1250, 400], [660, 180], [410, 250], [420, 555], [575, 665], [1150, 1160],
#         [700, 580], [685, 595], [685, 610], [770, 610], [795, 645], [720, 635],
#         [760, 650], [475, 960], [95, 260], [875, 920], [700, 500], [555, 815],
#         [830, 485], [1170, 65], [830, 610], [605, 625], [595, 360], [1340, 725], [1740, 245]
#     ])