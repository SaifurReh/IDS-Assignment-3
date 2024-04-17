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
            G.add_edge(i, j)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
plt.show()

# Check for loops
loops = list(nx.selfloop_edges(G))
if loops:
    print("There is a loop in the graph at point(s):", loops)
else:
    print("There are no loops in the graph.")
