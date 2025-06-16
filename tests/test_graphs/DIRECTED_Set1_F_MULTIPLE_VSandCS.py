import networkx as nx
import numpy as np

# create an empty undirected graph
F = nx.DiGraph()

# add nodes to the graph representing the nodes
F.add_node('v1', index=0, skip=False, supernode=[False, None])  # associate the index of the node it's super noded with
F.add_node('v2', index=1, skip=False, supernode=[False, None])
F.add_node('v3', index=2, skip=False, supernode=[False, None])
F.add_node('v4', index=3, skip=False, supernode=[False, None])
F.add_node('v5', index=4, skip=False, supernode=[False, None])

# A.add_node('GND', index=-2, supernode=[False, -1])
F.add_node('GND', index=-2)

# add edges to the graph representing the connections
F.add_edge('v3', 'v4', type='Csource', current=1, origin='v3')
F.add_edge('v2', 'v4', type='Csource', current=1, origin='v2')

F.add_edge('GND', 'v1', type='Vsource', voltage=3)
F.add_edge('GND', 'v5', type='Vsource', voltage=1)

F.add_edge('v1', 'v2', type='resistor', resistance=2)
F.add_edge('v2', 'v3', type='resistor', resistance=2)
F.add_edge('v3', 'v5', type='resistor', resistance=1)
F.add_edge('v4', 'GND', type='resistor', resistance=2)

for edge in F.edges(data=True):
    if edge[2]['type'] == 'resistor':
        F.add_edge(edge[1], edge[0], type='resistor', resistance=edge[2]['resistance'])
    if edge[2]['type'] == 'Csource':
        F.add_edge(edge[1], edge[0], type='Csource', current=edge[2]['current'], origin=edge[2]['origin'])
# print(F.adj['v5'])
