import networkx as nx

# create an empty undirected graph
A = nx.Graph()

# add nodes to the graph representing the nodes
A.add_node("R1", type="resistor", resistance=2)
A.add_node("R2", type="resistor", resistance=4)
A.add_node("R3", type="resistor", resistance=3)
A.add_node("R4", type="resistor", resistance=1)
A.add_node("R5", type="resistor", resistance=2)

A.add_node("V1", type="node", voltage=None, index=0)
A.add_node("V2", type="node", voltage=None, index=1)
A.add_node("V3", type="node", voltage=None, index=2)

A.add_node("GND", type="GND", voltage=0, index=-1)

A.add_node("VT", type="Vsource", voltage=1)

# add edges to the graph representing the connections
A.add_edge("VT", "V1")
A.add_edge("V1", "R1")
A.add_edge("V1", "R2")
A.add_edge("V2", "R1")
A.add_edge("V2", "R3")
A.add_edge("V2", "R4")
A.add_edge("V3", "R2")
A.add_edge("V3", "R3")
A.add_edge("V3", "R5")
A.add_edge("GND", "R4")
A.add_edge("GND", "R5")
A.add_edge("GND", "VT")

# print(A.nodes)
# print(list(A.neighbors("VT")))
