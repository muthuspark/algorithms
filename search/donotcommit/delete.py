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
np.random.seed(1)
# Generate array of random coodinates for city locations
coordinates = np.random.randint(0, 100, (20, 2))
print(coordinates)
cities = []
# Build Cities coordinates with their coordinates (x, y)
for c in coordinates:
    cities.append(City(c[0], c[1]))

# Set Simulated Annealing parameters
initial_temperature = 1000.0
cooling_rate = 0.995
num_iterations = 10000

# Solve the TSP using Simulated Annealing
best_tour, shortest_distance = simulated_annealing(cities, initial_temperature, cooling_rate, num_iterations)

# Print the best tour and its total distance
print("Best Tour:", best_tour)
print("Shortest Distance:", shortest_distance)