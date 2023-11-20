import numpy as np

# Generate some random data
data = np.random.randn(100, 2)
print(data)
# Calculate the distance between each point and the query point
query_point = np.array([0, 0])

# Calculate the Euclidean distance between each point in the data and the query point
distances = np.linalg.norm(data - query_point, axis=1)

# Sort the data by distance
sorted_data = np.array([data[i] for i in np.argsort(distances)])

# Get the nearest neighbors
nearest_neighbors = sorted_data[:5]

print(nearest_neighbors)
x = []
for row in nearest_neighbors:
    y = []
    for col in row:
        y.append(f"{col:.2f}")
    x.append(y)
print(x)