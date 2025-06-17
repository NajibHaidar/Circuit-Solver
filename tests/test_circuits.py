from src.graph_builder import GraphBuilder

def directed_h_3x3_simple():
    G = GraphBuilder.create_graph()
    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])
    GraphBuilder.add_edges(G, [
        ('GND', 'v1', {'type': 'Vsource', 'voltage': 6}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 1}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'GND', {'type': 'resistor', 'resistance': 3}),
    ])
    return G

def directed_set1_a():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('GND', 'v1', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'v3', {'type': 'resistor', 'resistance': 4}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 3}),
        ('v2', 'GND', {'type': 'resistor', 'resistance': 1}),
        ('v3', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_a_supernode():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v3', 'v1', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'GND', {'type': 'resistor', 'resistance': 4}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v2', 'GND', {'type': 'resistor', 'resistance': 3}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 1}),
        ('v3', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_b_cs():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v3', 'v2', {'type': 'Csource', 'current': 2, 'origin': 'v3'}),
        ('v1', 'GND', {'type': 'resistor', 'resistance': 3}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v1', 'v3', {'type': 'resistor', 'resistance': 4}),
        ('v2', 'GND', {'type': 'resistor', 'resistance': 1}),
        ('v3', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_c_vsandcs():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('v4', {'index': 3, 'skip': False, 'supernode': [False, -1]}),
        ('v5', {'index': 4, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v3', 'v4', {'type': 'Csource', 'current': 1, 'origin': 'v3'}),
        ('GND', 'v1', {'type': 'Vsource', 'voltage': 2}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v2', 'v4', {'type': 'resistor', 'resistance': 3}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v5', {'type': 'resistor', 'resistance': 1}),
        ('v5', 'GND', {'type': 'resistor', 'resistance': 1}),
        ('v4', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_e_multiple_vsandcs():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('v4', {'index': 3, 'skip': False, 'supernode': [False, -1]}),
        ('v5', {'index': 4, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v2', 'v5', {'type': 'Csource', 'current': 1, 'origin': 'v2'}),
        ('v4', 'GND', {'type': 'Csource', 'current': 2, 'origin': 'v4'}),
        ('GND', 'v1', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 1}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v4', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v5', {'type': 'resistor', 'resistance': 3}),
        ('v5', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_f_multiple_vsandcs():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('v4', {'index': 3, 'skip': False, 'supernode': [False, -1]}),
        ('v5', {'index': 4, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v3', 'v4', {'type': 'Csource', 'current': 1, 'origin': 'v3'}),
        ('v2', 'v4', {'type': 'Csource', 'current': 1, 'origin': 'v2'}),
        ('GND', 'v1', {'type': 'Vsource', 'voltage': 3}),
        ('GND', 'v5', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v5', {'type': 'resistor', 'resistance': 1}),
        ('v4', 'GND', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_i_noor():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('v4', {'index': 3, 'skip': False, 'supernode': [False, -1]}),
        ('v5', {'index': 4, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('GND', 'v2', {'type': 'Vsource', 'voltage': 3}),
        ('v4', 'v3', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'v4', {'type': 'resistor', 'resistance': 2}),
        ('GND', 'v1', {'type': 'resistor', 'resistance': 1}),
        ('v5', 'v1', {'type': 'resistor', 'resistance': 2}),
        ('v5', 'GND', {'type': 'resistor', 'resistance': 3}),
        ('v2', 'v5', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v2', {'type': 'resistor', 'resistance': 1}),
        ('GND', 'v4', {'type': 'resistor', 'resistance': 2}),
    ])

    return G

def directed_set1_i_supernode():
    G = GraphBuilder.create_graph()

    GraphBuilder.add_nodes(G, [
        ('v1', {'index': 0, 'skip': False, 'supernode': [False, -1]}),
        ('v2', {'index': 1, 'skip': False, 'supernode': [False, -1]}),
        ('v3', {'index': 2, 'skip': False, 'supernode': [False, -1]}),
        ('v4', {'index': 3, 'skip': False, 'supernode': [False, -1]}),
        ('v5', {'index': 4, 'skip': False, 'supernode': [False, -1]}),
        ('GND', {'index': -2}),
    ])

    GraphBuilder.add_edges(G, [
        ('v4', 'v3', {'type': 'Vsource', 'voltage': 3}),
        ('GND', 'v5', {'type': 'Vsource', 'voltage': 1}),
        ('v1', 'GND', {'type': 'resistor', 'resistance': 2}),
        ('GND', 'v4', {'type': 'resistor', 'resistance': 2}),
        ('v4', 'v1', {'type': 'resistor', 'resistance': 1}),
        ('v1', 'v2', {'type': 'resistor', 'resistance': 2}),
        ('v2', 'v3', {'type': 'resistor', 'resistance': 2}),
        ('v3', 'v5', {'type': 'resistor', 'resistance': 1}),
        ('v2', 'v4', {'type': 'resistor', 'resistance': 3}),
    ])

    return G
