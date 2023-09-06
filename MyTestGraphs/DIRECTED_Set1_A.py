import networkx as nx
import numpy as np

# create an empty undirected graph
A = nx.DiGraph()

# add nodes to the graph representing the nodes
A.add_node('v1', index=0, skip=False, supernode=[False, -1])  # associate the index of the node it's super noded with
A.add_node('v2', index=1, skip=False, supernode=[False, -1])
A.add_node('v3', index=2, skip=False, supernode=[False, -1])

# A.add_node('GND', index=-2, supernode=[False, -1])
A.add_node('GND', index=-2)

# add edges to the graph representing the connections
A.add_edge('GND', 'v1', type='Vsource', voltage=1)
A.add_edge('v1', 'v3', type='resistor', resistance=4)
A.add_edge('v1', 'v2', type='resistor', resistance=2)
A.add_edge('v2', 'v3', type='resistor', resistance=3)
A.add_edge('v2', 'GND', type='resistor', resistance=1)
A.add_edge('v3', 'GND', type='resistor', resistance=2)

for edge in A.edges(data=True):
    if edge[2]['type'] == 'resistor':
        A.add_edge(edge[1], edge[0], type='resistor', resistance=edge[2]['resistance'])

# print(A.nodes)
# print("After Adding: ")

# print(list(A.edges(data=True)))
# print(list(A.nodes(data=True)))
# print()

# print(list(A.neighbors('v1')))
# print(A.edges('v2', data=True))
# print(A.nodes.get('v1'))
# A.nodes.get('v1')['supernode'] = [True, 1]
# print(A.nodes.get('v1'))
# print(A.nodes(data=True))
# print(A.nodes.get('v1')['index'])
# print({1, 2, 3, 2, 3})
# print(list(A.neighbors('GND')))
# print(list(A['v3'].items()))
# for edge in A.adj['v3']:
#     print(A.edges(edge, data=True))

# print(len(A.edges))

# I = np.array(np.zeros((3, 1)))
# I[1][0] = 1
# print(I)
