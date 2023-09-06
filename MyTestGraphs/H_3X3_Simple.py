import networkx as nx

# create an empty undirected graph
H = nx.Graph()

# add nodes to the graph representing the nodes
H.add_node("R1", type="resistor", resistance=1)
H.add_node("R2", type="resistor", resistance=2)
H.add_node("R3", type="resistor", resistance=3)

H.add_node("V1", type="node", voltage=None, index=0)
H.add_node("V2", type="node", voltage=None, index=1)
H.add_node("V3", type="node", voltage=None, index=2)

H.add_node("GND", type="GND", voltage=0, index=-1)

H.add_node("VT", type="Vsource", voltage=6)

# add edges to the graph representing the connections
H.add_edge("VT", "V1")
H.add_edge("V1", "R1")
H.add_edge("R1", "V2")
H.add_edge("V2", "R2")
H.add_edge("R2", "V3")
H.add_edge("V3", "R3")
H.add_edge("R3", "GND")
H.add_edge("GND", "VT")
