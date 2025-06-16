import networkx as nx

# create an empty undirected graph
B = nx.Graph()

# add nodes to the graph representing the nodes
B.add_node("R1", type="resistor", resistance=3)
B.add_node("R2", type="resistor", resistance=4)
B.add_node("R3", type="resistor", resistance=2)
B.add_node("R4", type="resistor", resistance=1)
B.add_node("R5", type="resistor", resistance=2)

B.add_node("V1", type="node", voltage=None, index=0)
B.add_node("V2", type="node", voltage=None, index=1)
B.add_node("V3", type="node", voltage=None, index=2)

B.add_node("GND", type="GND", voltage=0, index=-1)

# B.add_node("VT", type="Isource", current=2)
B.add_node("VT", type="Vsource", voltage=2)

# add edges to the graph representing the connections
# B.add_edge("R1", "V1")
# B.add_edge("V1", "R2")
# B.add_edge("V1", "R3")
# B.add_edge("R2", "GND")
# B.add_edge("R3", "V2")
# B.add_edge("V2", "VT")
# B.add_edge("GND", "VT")
# B.add_edge("V2", "R4")
# B.add_edge("GND", "R5")
# B.add_edge("R4", "V3")
# B.add_edge("R5", "V3")
# B.add_edge("V3", "R1")

B.add_edge("R1", "V1")
B.add_edge("V1", "R2")
B.add_edge("V1", "R3")
B.add_edge("R2", "GND")
B.add_edge("R3", "V3")
B.add_edge("V3", "VT")
B.add_edge("GND", "VT")
B.add_edge("V3", "R4")
B.add_edge("GND", "R5")
B.add_edge("R4", "V2")
B.add_edge("R5", "V2")
B.add_edge("V2", "R1")









