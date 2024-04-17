import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array([
    [0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
])

# Create an empty graph
G = nx.Graph()

# Add edges to the graph based on the adjacency matrix
for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            # Assign random weight to the edge
            weight = np.random.randint(1, 10)  # You can adjust the range of random weights as needed
            G.add_edge(i, j, weight=weight)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
plt.show()

# Find shortest path using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, source=0, target=1, weight='weight')
shortest_path_length = nx.dijkstra_path_length(G, source=0, target=1, weight='weight')

# Print shortest path and its length
print("Shortest path between nodes A and B:", shortest_path)
print("Length of the shortest path:", shortest_path_length)
