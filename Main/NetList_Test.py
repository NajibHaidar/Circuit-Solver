from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import networkx as nx

# create a circuit
circuit = Circuit('Example Circuit')

# add components to the circuit
circuit.R(1, 'v1', 'v2', unit('1Ohm'))
circuit.C(1, 'v1', 'v2', unit('1Ohm'))
circuit.R(5, 'v1', 'v2', unit('1Ohm'))

print(circuit)
simulator = circuit.simulator()

# # create a directed graph
# G = nx.DiGraph()
#
# # add nodes to the graph
# nodes = list(set([c.node1 for c in circuit.components] + [c.node2 for c in circuit.components]))
# G.add_nodes_from(nodes)
#
# # add edges to the graph
# for c in circuit.components:
#     G.add_edge(c.node1, c.node2, component=c)
#
# # print the graph information
# print("Nodes: ", G.nodes())
# print("Edges: ", G.edges())

