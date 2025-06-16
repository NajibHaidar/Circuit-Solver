import networkx as nx
import numpy as np

# create an empty undirected graph
B = nx.DiGraph()

# add nodes to the graph representing the nodes
B.add_node('v1', index=0, skip=False, supernode=[False, None])  # associate the index of the node it's super noded with
B.add_node('v2', index=1, skip=False, supernode=[False, None])
B.add_node('v3', index=2, skip=False, supernode=[False, None])

# A.add_node('GND', index=-2, supernode=[False, -1])
B.add_node('GND', index=-2)

# add edges to the graph representing the connections
B.add_edge('v3', 'v2', type='Csource', current=2, origin='v3')

B.add_edge('v1', 'GND', type='resistor', resistance=3)
B.add_edge('v1', 'v2', type='resistor', resistance=2)
B.add_edge('v1', 'v3', type='resistor', resistance=4)
B.add_edge('v2', 'GND', type='resistor', resistance=1)
B.add_edge('v3', 'GND', type='resistor', resistance=2)

for edge in B.edges(data=True):
    if edge[2]['type'] == 'resistor':
        B.add_edge(edge[1], edge[0], type='resistor', resistance=edge[2]['resistance'])
    if edge[2]['type'] == 'Csource':
        B.add_edge(edge[1], edge[0], type='Csource', current=2, origin=edge[0])
