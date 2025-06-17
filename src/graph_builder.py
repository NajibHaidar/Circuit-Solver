import networkx as nx

class GraphBuilder:
    @staticmethod
    def create_graph():
        return nx.DiGraph()
    
    @staticmethod
    def create_standard_nodes(graph, num_nodes):
        nodes = [
            (f'v{i+1}', {'index': i, 'skip': False, 'supernode': [False, -1]})
            for i in range(num_nodes)
        ]
        nodes.append(('GND', {'index': -2}))
        GraphBuilder.add_nodes(graph, nodes)

    @staticmethod
    def add_nodes(graph, nodes):
        for name, attrs in nodes:
            graph.add_node(name, **attrs)

    @staticmethod
    def add_components(graph, components):
        for component in components:
            component.add_to_graph(graph)
