import networkx as nx
import random
import json 
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, num_edges):
    # Create an empty directed graph
    G = nx.DiGraph()

    # Add nodes to the graph
    for node in range(num_nodes):
        G.add_node(node)

    # Add random weighted edges to the graph
    for _ in range(num_edges):
        source = random.randint(0, num_nodes - 1)
        target = random.randint(0, num_nodes - 1)
        weight = random.randint(1, 10)  # Adjust the weight range as needed
        G.add_edge(source, target, weight=weight)

    return G

# Example usage:
random_graph = generate_random_graph(10, 20)
nx.draw_networkx(random_graph, arrows=True)