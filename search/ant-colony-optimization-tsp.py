import numpy as np


class AntColony:
    def __init__(self, distance_matrix, num_ants, 
                    num_iterations, decay_rate, alpha=1.0, beta=2.0):
        self.distance_matrix = distance_matrix
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay_rate = decay_rate
        self.alpha = alpha
        self.beta = beta
        self.num_cities = distance_matrix.shape[0]
        self.pheromone_matrix = np.ones(
                            (self.num_cities, self.num_cities))
        self.best_path = None
        self.best_path_length = float('inf')

    def run(self):
        for iteration in range(self.num_iterations):
            paths = self.construct_paths()
            self.update_pheromone(paths)
            best_path_index = np.argmin(
                [self.path_length(path) for path in paths])
            if (self.path_length(paths[best_path_index]) 
                    < self.best_path_length):
                self.best_path = paths[best_path_index]
                self.best_path_length = self.path_length(
                    paths[best_path_index])

            self.pheromone_matrix *= self.decay_rate
            print(self.best_path_length)

    def construct_paths(self):
        paths = []
        for ant in range(self.num_ants):
            visited = [0]  # Start from city 0
            cities_to_visit = set(range(1, self.num_cities))
            while cities_to_visit:
                next_city = self.select_next_city(visited[-1], 
                                                cities_to_visit)
                visited.append(next_city)
                cities_to_visit.remove(next_city)
            paths.append(visited)
        return paths

    def select_next_city(self, current_city, cities_to_visit):
        pheromone_values = [
            self.pheromone_matrix[current_city][next_city] ** self.alpha
                            for next_city in cities_to_visit]
        heuristic_values = [
            1.0 / self.distance_matrix[current_city][next_city] ** self.beta
                            for next_city in cities_to_visit]
        probabilities = np.array(pheromone_values) * np.array(
                                                        heuristic_values)
        probabilities /= np.sum(probabilities)
        return list(cities_to_visit)[
                            np.random.choice(range(len(cities_to_visit)), 
                                                p=probabilities)]

    def update_pheromone(self, paths):
        for path in paths:
            path_length = self.path_length(path)
            for i in range(len(path) - 1):
                current_city, next_city = path[i], path[i + 1]
                self.pheromone_matrix[current_city][next_city] += 1.0 / path_length

    def path_length(self, path):
        length = 0
        for i in range(len(path) - 1):
            current_city, next_city = path[i], path[i + 1]
            length += self.distance_matrix[current_city][next_city]
        return length


def euclidean_distance(c1, c2):
    # This method calculates the Euclidean distance between two points.
    return np.linalg.norm(c1 - c2)


def adjacency_matrix(coordinate):
    # This method calculates the adjacency matrix for a 
    # given set of coordinates.
    # The adjacency matrix represents the distances between 
    # each pair of coordinates.
    # It takes a list of coordinates as input and returns a
    # numpy array representing the adjacency matrix.
    matrix = np.zeros((len(coordinate), len(coordinate)))
    for i in range(len(coordinate)):
        for j in range(i + 1, len(coordinate)):
            p = euclidean_distance(coordinate[i], coordinate[j])
            matrix[i][j] = p
            matrix[j][i] = p
    return matrix


# Latitude longitude of cities.
berlin52 = np.array([[3.3333, 36.6667],
                     [6.1333, 35.75],
                     [2.8, 32.2],
                     [1.5, 34.5333],
                     [8.9, 33.4833],
                     [5.8333, 29.25],
                     [6.8333, 37.6667],
                     [7.8, 35.43],
                     [2, 31.5],
                     [6.8333, 31.1667],
                     [5, 30],
                     [3.1167, 37.3333],
                     [10.3333, 40.3333],
                     [2.5, 32.9667],
                     [9.3333, 34.8333],
                     [6.8333, 39.2],
                     [5, 39.6167],
                     [7, 39],
                     [9.9667, 39.6333],
                     [6.3333, 30],
                     [7.9667, 32.4833],
                     [4.1667, 34.25],
                     [7, 31.5],
                     [10.3333, 36],
                     [5.75, 34.9833],
                     [2.1667, 37.6],
                     [6, 34.5],
                     [5.0333, 32.8333],
                     [5.0833, 39.0333],
                     [5.04, 39.43]])

distance_matrix = adjacency_matrix(berlin52)

# Set the parameters
num_ants = 10
num_iterations = 100
decay_rate = 0.5

# Create the AntColony instance and run the algorithm
aco = AntColony(distance_matrix, num_ants, num_iterations, decay_rate)
aco.run()

# Get the best path found
best_path = aco.best_path
best_path_length = aco.best_path_length

# Print the result
print("Best Path:", best_path)
print("Best Path Length:", best_path_length)
