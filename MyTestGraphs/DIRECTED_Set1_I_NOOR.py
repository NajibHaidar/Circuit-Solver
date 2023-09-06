import networkx as nx
import numpy as np

# create an empty undirected graph
N = nx.DiGraph()

# add nodes to the graph representing the nodes
N.add_node('v1', index=0, skip=False, supernode=[False, None])  # associate the index of the node it's super noded with
N.add_node('v2', index=1, skip=False, supernode=[False, None])
N.add_node('v3', index=2, skip=False, supernode=[False, None])
N.add_node('v4', index=3, skip=False, supernode=[False, None])
N.add_node('v5', index=4, skip=False, supernode=[False, None])

# A.add_node('GND', index=-2, supernode=[False, -1])
N.add_node('GND', index=-2)

# add edges to the graph representing the connections
N.add_edge('GND', 'v2', type='Vsource', voltage=3)
N.add_edge('v4', 'v3', type='Vsource', voltage=1)

N.add_edge('v1', 'v4', type='resistor', resistance=2)
N.add_edge('GND', 'v1', type='resistor', resistance=1)
N.add_edge('v5', 'v1', type='resistor', resistance=2)
N.add_edge('v5', 'GND', type='resistor', resistance=3)
N.add_edge('v2', 'v5', type='resistor', resistance=2)
N.add_edge('v3', 'v2', type='resistor', resistance=1)
N.add_edge('GND', 'v4', type='resistor', resistance=2)

for edge in N.edges(data=True):
    if edge[2]['type'] == 'resistor':
        N.add_edge(edge[1], edge[0], type='resistor', resistance=edge[2]['resistance'])

# print(N.adj['v5'])

