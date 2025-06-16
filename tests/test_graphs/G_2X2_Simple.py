import networkx as nx

# create an empty undirected graph
G = nx.Graph()

# add nodes to the graph representing the nodes
G.add_node("R1", type="resistor", resistance=1)
G.add_node("R2", type="resistor", resistance=2)

G.add_node("V1", type="node", voltage=None, index=0)
G.add_node("V2", type="node", voltage=None, index=1)

G.add_node("GND", type="GND", voltage=0, index=-1)

G.add_node("VT", type="Vsource", voltage=3)

# add edges to the graph representing the connections
G.add_edge("VT", "V1")
G.add_edge("V1", "R1")
G.add_edge("R1", "V2")
G.add_edge("V2", "R2")
G.add_edge("R2", "GND")
G.add_edge("VT", "GND")