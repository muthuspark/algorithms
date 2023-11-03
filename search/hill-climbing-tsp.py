# Author: Muthukrishnan
# Algorithm: Hill Climbing TSP
import numpy as np


def euclidean_distance(c1, c2):
    # This method calculates the Euclidean distance between two points.
    # It takes two points, c1 and c2, as input and returns the Euclidean distance between them.
    # The Euclidean distance is calculated using the numpy.linalg.norm function.
    # The function subtracts c2 from c1 and calculates the norm of the resulting vector.
    # The norm represents the length of the vector, which is the Euclidean distance between c1 and c2.
    return np.linalg.norm(c1 - c2)


def adjacency_matrix(coordinate):
    # This method calculates the adjacency matrix for a given set of coordinates.
    # The adjacency matrix represents the distances between each pair of coordinates.
    # It takes a list of coordinates as input and returns a
    # numpy array representing the adjacency matrix.
    matrix = np.zeros((len(coordinate), len(coordinate)))
    for i in range(len(coordinate)):
        for j in range(i + 1, len(coordinate)):
            p = euclidean_distance(coordinate[i], coordinate[j])
            matrix[i][j] = p
            matrix[j][i] = p
    return matrix


def solution(matrix):
    # This method generates a random solution for the TSP problem.
    # It takes the adjacency matrix as input and returns a random
    # permutation of the indices of the matrix.
    # The random permutation represents a random path through the cities.
    # This method is used as an initial solution for the hill climbing
    # algorithm.
    return np.random.permutation(len(matrix))


def total_distance_of_path(matrix, solution):
    # This method calculates the length of the path for a given solution.
    # It takes the adjacency matrix and the solution as input and returns
    # the sum of the distances between each pair of consecutive cities in the
    # solution
    return sum(matrix[solution[i]][solution[i - 1]]
               for i in range(len(solution)))


def get_neighbors(solution):
    # This method generates the neighbors of a given solution.
    # It takes the solution as input and returns a list of all possible
    # solutions that can be obtained by swapping two cities in the solution.
    # Each neighbor is obtained by swapping the positions of two cities in the solution.
    # The neighbors are generated by iterating over each pair of cities in the solution
    # and swapping their positions.
    # The method returns a list of all the generated neighbors.
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors


def best_neighbors(matrix, solution):
    # This method calculates the best neighbors of a given solution.
    # It takes the adjacency matrix and the solution as input and returns
    # the best neighbor and its route length.
    # The method starts by generating all possible neighbors of the solution
    # using the get_neighbors() method.
    # It then initializes the best neighbor and its route length with the first neighbor.
    # The method iterates over each neighbor and calculates the route length for each neighbor
    # using the total_distance_of_path() method.
    # If the route length of the current neighbor is less than the route length of the best neighbor,
    # the best neighbor and its route length are updated to the current neighbor.
    # Finally, the method returns the best neighbor and its route length.
    neighbors = get_neighbors(solution)
    best_neighbour = neighbors[0]
    best_route_length = total_distance_of_path(matrix, best_neighbour)
    for neighbour in neighbors:
        current_route_length = total_distance_of_path(matrix, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length


def hill_climbing(coordinate):
    # This method implements the hill climbing algorithm to solve the TSP problem.
    # It takes the coordinate of the points/cities as input and returns the best path
    # and its distance.
    # The algorithm starts by generating a random initial solution using the solution() method.
    # It then calculates the total distance of the initial solution using the total_distance_of_path() method.
    # The algorithm then enters a loop where it generates the best neighbor of the current solution
    # using the best_neighbors() method. If the distance of the best neighbor is less than the current distance,
    # the current solution is updated to the best neighbor and the current distance is updated to the distance of the best neighbor.
    # The loop continues until the distance of the best neighbor is no longer less than the current distance.
    # Finally, the algorithm returns the current distance and the current
    # solution, which represents the best path.
    distance_matrix = adjacency_matrix(coordinate)
    current_solution = solution(distance_matrix)
    current_distance = total_distance_of_path(distance_matrix, current_solution)
    best_neighbor, best_neighbor_path = best_neighbors(
        distance_matrix, current_solution)

    while best_neighbor_path < current_distance:
        current_solution = best_neighbor
        current_distance = best_neighbor_path
        best_neighbor, best_neighbor_path = best_neighbors(
            distance_matrix, current_solution)

    return current_distance, current_solution


# coordinate of the points/cities
coordinate = np.array([
        [565, 575], [25, 185], [345, 750], [945, 685], [845, 655],
        [880, 660], [25, 230], [525, 1000], [580, 1175], [650, 1130],
        [1605, 620], [1220, 580], [1465, 200], [1530, 5], [845, 680],
        [725, 370], [145, 665], [415, 635], [510, 875], [560, 365], [300, 465],
        [520, 585], [480, 415], [835, 625], [975, 580], [1215, 245], [1320, 315],
        [1250, 400], [660, 180], [410, 250], [420, 555], [575, 665], [1150, 1160],
        [700, 580], [685, 595], [685, 610], [770, 610], [795, 645], [720, 635],
        [760, 650], [475, 960], [95, 260], [875, 920], [700, 500], [555, 815],
        [830, 485], [1170, 65], [830, 610], [605, 625], [595, 360], [1340, 725], [1740, 245]
    ])
# coordinate = np.array([[50, 98], [54, 6], [34, 66], [63, 52], [39, 62], [46, 75], [28, 65], [18, 37], [18, 97], [13, 80]])

final_solution = hill_climbing(coordinate)
print(
    f"The best path is {final_solution[1]} whose distance is {final_solution[0]}")
