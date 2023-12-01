import random
import math
import numpy as np

# Define a class to represent a city with x and y coordinates
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define a function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

# Define the objective function to calculate the total tour length
def total_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Simulated Annealing function to find the best tour
def simulated_annealing(cities, initial_temperature, cooling_rate, num_iterations):
    num_cities = len(cities)
    
    # Initialize a random tour
    current_tour = random.sample(range(num_cities), num_cities)
    best_tour = current_tour.copy()
    
    current_temperature = initial_temperature
    
    for iteration in range(num_iterations):
        # Perturb the current tour by swapping two random cities
        new_tour = current_tour.copy()
        i, j = random.sample(range(num_cities), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        # Calculate the cost of the current and new tours
        current_cost = total_distance(current_tour, cities)
        new_cost = total_distance(new_tour, cities)
        
        # Decide whether to accept the new tour based on cost and temperature
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temperature):
            current_tour = new_tour.copy()
            if new_cost < total_distance(best_tour, cities):
                best_tour = new_tour.copy()
        
        # Reduce the temperature
        current_temperature *= cooling_rate
    
    return best_tour, total_distance(best_tour, cities)

# Example usage
if __name__ == "__main__":
    np.random.seed(1)
    # Generate array of random coodinates for city locations
    coordinates = np.random.randint(0, 100, (20, 2))
    cities = []
    # Build Cities coordinates with their coordinates (x, y)
    for c in coordinates:
        cities.append(City(c[0], c[1]))
    
    # Set Simulated Annealing parameters
    initial_temperature = 1000.0
    cooling_rate = 0.995
    num_iterations = 10000
    
    # Solve the TSP using Simulated Annealing
    best_tour, shortest_distance = simulated_annealing(cities, 
                                                       initial_temperature, 
                                                       cooling_rate, 
                                                       num_iterations)
    
    # Print the best tour and its total distance
    print("Best Tour:", best_tour)
    print("Shortest Distance:", shortest_distance) 


# Example usage
if __name__ == "__main__":
    np.random.seed(1)
    # Generate array of random coodinates for city locations
    coordinates = [
        [565, 575], [25, 185], [345, 750], [945, 685], [845, 655],
        [880, 660], [25, 230], [525, 1000], [580, 1175], [650, 1130],
        [1605, 620], [1220, 580], [1465, 200], [1530, 5], [845, 680],
        [725, 370], [145, 665], [415, 635], [510, 875], [560, 365], [300, 465],
        [520, 585], [480, 415], [835, 625], [
            975, 580], [1215, 245], [1320, 315],
        [1250, 400], [660, 180], [410, 250], [
            420, 555], [575, 665], [1150, 1160],
        [700, 580], [685, 595], [685, 610], [770, 610], [795, 645], [720, 635],
        [760, 650], [475, 960], [95, 260], [875, 920], [700, 500], [555, 815],
        [
            830, 485], [
            1170, 65], [
            830, 610], [
                605, 625], [
                    595, 360], [
                        1340, 725], [
                            1740, 245]
    ]
    cities = []
    # Build Cities coordinates with their coordinates (x, y)
    for c in coordinates:
        cities.append(City(c[0], c[1]))

    # Set Simulated Annealing parameters
    initial_temperature = 1000.0
    cooling_rate = 0.995
    num_iterations = 10000

    # Solve the TSP using Simulated Annealing
    best_tour, shortest_distance = simulated_annealing(
        cities, initial_temperature, cooling_rate, num_iterations)

    # Print the best tour and its total distance
    print("Best Tour:", best_tour)
    print("Shortest Distance:", shortest_distance)
