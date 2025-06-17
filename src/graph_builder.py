import networkx as nx

class GraphBuilder:
    @staticmethod
    def create_graph():
        return nx.DiGraph()

    @staticmethod
    def add_nodes(graph, nodes):
        for name, attrs in nodes:
            graph.add_node(name, **attrs)

    @staticmethod
    def add_edges(graph, edges):
        for src, dst, attrs in edges:
            graph.add_edge(src, dst, **attrs)

            # Mirror resistor and Csource edges
            if attrs.get("type") in ("resistor", "Csource"):
                graph.add_edge(dst, src, **attrs)
