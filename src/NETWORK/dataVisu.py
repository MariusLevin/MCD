import networkx as nx
import matplotlib.pyplot as plt

data = {'a1': ['a2'], 'a2': ['a1', 'a3', 'a4'], 'a3': ['a2'], 'a4': ['a2'], 'a5': []}

# Create graph
G = nx.Graph()

# Create nodes
G.add_nodes_from(data.keys())

# Create edges
for key in data.keys():
    for value in data[key]:
        G.add_edge(key, value, name='ok')

# Draw graph
nx.draw_networkx(G)
plt.show()