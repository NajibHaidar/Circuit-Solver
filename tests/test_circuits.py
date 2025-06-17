from src.graph_builder import GraphBuilder
from src.components import Resistor, Csource, Vsource

def directed_h_3x3_simple():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 3)  # v1 to v3 + GND

    components = [
        Vsource('GND', 'v1', 6),
        Resistor('v1', 'v2', 1),
        Resistor('v2', 'v3', 2),
        Resistor('v3', 'GND', 3),
    ]

    GraphBuilder.add_components(G, components)

    return G

def directed_set1_a():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 3)  # v1 to v3 + GND

    components = [
        Vsource('GND', 'v1', 1),
        Resistor('v1', 'v3', 4),
        Resistor('v1', 'v2', 2),
        Resistor('v2', 'v3', 3),
        Resistor('v2', 'GND', 1),
        Resistor('v3', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_a_supernode():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 3)  # v1 to v3 + GND

    components = [
        Vsource('v3', 'v1', 1),
        Resistor('v1', 'GND', 4),
        Resistor('v1', 'v2', 2),
        Resistor('v2', 'GND', 3),
        Resistor('v2', 'v3', 1),
        Resistor('v3', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_b_cs():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 3)  # v1 to v3 + GND

    components = [
        Csource('v3', 'v2', 2, 'v3'),
        Resistor('v1', 'GND', 3),
        Resistor('v1', 'v2', 2),
        Resistor('v1', 'v3', 4),
        Resistor('v2', 'GND', 1),
        Resistor('v3', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_c_vsandcs():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 5)  # v1 to v5 + GND

    components = [
        Csource('v3', 'v4', 1, 'v3'),
        Vsource('GND', 'v1', 2),
        Resistor('v1', 'v2', 2),
        Resistor('v2', 'v4', 3),
        Resistor('v2', 'v3', 2),
        Resistor('v3', 'v5', 1),
        Resistor('v5', 'GND', 1),
        Resistor('v4', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_e_multiple_vsandcs():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 5)  # v1 to v5 + GND

    components = [
        Csource('v2', 'v5', 1, 'v2'),
        Csource('v4', 'GND', 2, 'v4'),
        Vsource('GND', 'v1', 1),
        Resistor('v1', 'v2', 1),
        Resistor('v2', 'v3', 2),
        Resistor('v3', 'v4', 2),
        Resistor('v3', 'v5', 3),
        Resistor('v5', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_f_multiple_vsandcs():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 5)  # v1 to v5 + GND

    components = [
        Csource('v3', 'v4', 1, 'v3'),
        Csource('v2', 'v4', 1, 'v2'),
        Vsource('GND', 'v1', 3),
        Vsource('GND', 'v5', 1),
        Resistor('v1', 'v2', 2),
        Resistor('v2', 'v3', 2),
        Resistor('v3', 'v5', 1),
        Resistor('v4', 'GND', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_i_noor():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 5)  # v1 to v5 + GND

    components = [
        Vsource('GND', 'v2', 3),
        Vsource('v4', 'v3', 1),
        Resistor('v1', 'v4', 2),
        Resistor('GND', 'v1', 1),
        Resistor('v5', 'v1', 2),
        Resistor('v5', 'GND', 3),
        Resistor('v2', 'v5', 2),
        Resistor('v3', 'v2', 1),
        Resistor('GND', 'v4', 2),
    ]

    GraphBuilder.add_components(G, components)
    return G

def directed_set1_i_supernode():
    G = GraphBuilder.create_graph()
    GraphBuilder.create_standard_nodes(G, 5) # v1 to v5 + GND

    components = [
        Vsource('v4', 'v3', 3),
        Vsource('GND', 'v5', 1),
        Resistor('v1', 'GND', 2),
        Resistor('GND', 'v4', 2),
        Resistor('v4', 'v1', 1),
        Resistor('v1', 'v2', 2),
        Resistor('v2', 'v3', 2),
        Resistor('v3', 'v5', 1),
        Resistor('v2', 'v4', 3),
    ]

    GraphBuilder.add_components(G, components)

    return G
