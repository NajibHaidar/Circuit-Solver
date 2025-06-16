import networkx as nx

# create an empty undirected graph
H = nx.DiGraph()

# add nodes to the graph representing the nodes
H.add_node('v1', index=0, skip=False, supernode=[False, -1])  # associate the index of the node it's super noded with
H.add_node('v2', index=1, skip=False, supernode=[False, -1])
H.add_node('v3', index=2, skip=False, supernode=[False, -1])

# A.add_node('GND', index=-2, supernode=[False, -1])
H.add_node('GND', index=-2)

# add edges to the graph representing the connections
H.add_edge('GND', 'v1', type='Vsource', voltage=6)
H.add_edge('v1', 'v2', type='resistor', resistance=1)
H.add_edge('v2', 'v3', type='resistor', resistance=2)
H.add_edge('v3', 'GND', type='resistor', resistance=3)

for edge in H.edges(data=True):
    if edge[2]['type'] == 'resistor':
        H.add_edge(edge[1], edge[0], type='resistor', resistance=edge[2]['resistance'])
