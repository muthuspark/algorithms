import random
import numpy as np


def calculate_distance(c1, c2):
    """
    Calculate the euclidean distance between two points.

    Args:
        c1 (numpy.ndarray): The coordinates of the first point.
        c2 (numpy.ndarray): The coordinates of the second point.

    Returns:
        float: The distance between the two points.
    """
    return np.linalg.norm(c2-c1)


def calculate_cost(perm, cities):
    # Calculate the cost of the given permutation
    # by summing the distances between consecutive cities
    total_distance = 0
    for i, c1 in enumerate(perm):
        c2 = perm[0] if i == len(perm) - 1 else perm[i + 1]
        total_distance += calculate_distance(cities[c1], cities[c2])
    return total_distance


def random_permutation(cities):
    return random.sample(range(len(cities)), len(cities))


def stochastic_two_opt(parent):
    permutation = parent.copy()
    length_limit = len(permutation) - 1
    c1, c2 = random.sample(range(len(permutation)), 2)
    exclude = [c1]
    exclude.append(permutation[length_limit] if c1 == 0 else c1 - 1)
    exclude.append(0 if c1 == length_limit else c1 + 1)
    while c2 in exclude:
        c2 = random.randint(0, length_limit)
    c1, c2 = min(c1, c2), max(c1, c2)
    permutation[c1:c2] = reversed(permutation[c1:c2])
    return permutation, [(parent[c1 - 1], parent[c1]), (parent[c2 - 1], parent[c2])]


def is_tabu(permutation, tabu_list):
    for i, c1 in enumerate(permutation):
        c2 = permutation[0] if i == len(
            permutation) - 1 else permutation[i + 1]
        if [c1, c2] in tabu_list:
            return True
    return False


def generate_neighbor(best, tabu_list, cities):
    perm, edges = None, None
    while perm is None or is_tabu(perm, tabu_list):
        perm, edges = stochastic_two_opt(best['path'])
    neighbor = {'path': perm}
    neighbor['cost'] = calculate_cost(neighbor['path'], cities)
    return neighbor, edges


def search(cities, tabu_list_size, neighbor_list_size, max_iter):
    current_solution = {'path': random_permutation(cities)}
    current_solution['cost'] = calculate_cost(current_solution['path'], cities)
    best = current_solution
    tabu_list = []
    for iter in range(max_iter):
        neighbors = [
            generate_neighbor(
                current_solution,
                tabu_list,
                cities) for i in range(neighbor_list_size)]
        neighbors.sort(key=lambda x: x[0]['cost'])
        print("\n", neighbors , "\n")
        best_neighbor = neighbors[0][0]
        best_neighbor_edges = neighbors[0][1]
        if best_neighbor['cost'] < current_solution['cost']:
            current_solution = best_neighbor
            if best_neighbor['cost'] < best['cost']:
                best = best_neighbor
            tabu_list.extend(best_neighbor_edges)
            while len(tabu_list) > tabu_list_size:
                tabu_list.pop(0)
        print(f"\nIteration {iter + 1}, best={best['cost']}, path={best['path']}")
    return best


if __name__ == '__main__':
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
    max_iter = 500
    tabu_list_size = 10
    max_neighbors = 10
    best = search(berlin52, tabu_list_size, max_neighbors, max_iter)
    print(
        f"The best path is {best['path']} whose distance is {round(best['cost'])}")
