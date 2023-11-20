import random
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate distance between two cities
def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Function to calculate total distance of a route
def calculate_total_distance(route, cities):
    total_distance = 0.0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]])  # Return to starting city
    return total_distance

# Function to create initial population
def create_initial_population(population_size, num_cities):
    population = []
    for _ in range(population_size):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population

# Function for selection: choosing the most fit individuals
def selection(population, num_parents, cities):
    sorted_population = sorted(population, key=lambda x: calculate_total_distance(x, cities))
    return sorted_population[:num_parents]

# Function for crossover: combining genetic material from parents
def crossover(parents, num_offspring):
    offspring = []
    for _ in range(num_offspring):
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(0, len(parent1) - 1)
        child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        offspring.append(child)
    return offspring

# Function for mutation: introducing random changes in offspring
def mutation(offspring, mutation_rate):
    mutated_offspring = []
    for child in offspring:
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(child)), 2)
            child[idx1], child[idx2] = child[idx2], child[idx1]  # Swap cities
        mutated_offspring.append(child)
    return mutated_offspring

# Genetic Algorithm for TSP
def genetic_algorithm_for_tsp(cities, population_size, num_generations, num_parents, mutation_rate):
    num_cities = len(cities)
    population = create_initial_population(population_size, num_cities)

    for generation in range(num_generations):
        parents = selection(population, num_parents, cities)
        offspring = crossover(parents, population_size - num_parents)
        mutated_offspring = mutation(offspring, mutation_rate)
        population = parents + mutated_offspring

        best_route = min(population, key=lambda x: calculate_total_distance(x, cities))
        best_distance = calculate_total_distance(best_route, cities)
        print(f"Generation {generation+1}: Best Distance = {best_distance}")

    best_route.append(best_route[0])  # Return to starting city to complete the loop
    return best_route, best_distance

# Example cities
cities = [[3.3333, 36.6667],
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
                         [5.04, 39.43]]

# Genetic Algorithm parameters
population_size = 100
num_generations = 500
num_parents = 20
mutation_rate = 0.1

# Run the Genetic Algorithm
best_route, best_distance = genetic_algorithm_for_tsp(cities, population_size, num_generations, num_parents, mutation_rate)

# Plotting the best route
x_vals = [city[0] for city in cities]
y_vals = [city[1] for city in cities]
plt.scatter(x_vals, y_vals)
for i in range(len(best_route) - 1):
    plt.plot([cities[best_route[i]][0], cities[best_route[i + 1]][0]],
             [cities[best_route[i]][1], cities[best_route[i + 1]][1]], 'k-')
plt.title(f"Best Route: Distance = {best_distance}")
plt.show()