class Component:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def add_to_graph(self, graph):
        raise NotImplementedError


class Resistor(Component):
    def __init__(self, src, dst, resistance):
        super().__init__(src, dst)
        self.resistance = resistance

    def add_to_graph(self, graph):
        attrs = {'type': 'resistor', 'resistance': self.resistance}
        graph.add_edge(self.src, self.dst, **attrs)
        graph.add_edge(self.dst, self.src, **attrs)  # symmetrical


class Csource(Component):
    def __init__(self, src, dst, current, origin):
        super().__init__(src, dst)
        self.current = current
        self.origin = origin

    def add_to_graph(self, graph):
        attrs = {'type': 'Csource', 'current': self.current, 'origin': self.origin}
        graph.add_edge(self.src, self.dst, **attrs)
        graph.add_edge(self.dst, self.src, **attrs)


class Vsource(Component):
    def __init__(self, src, dst, voltage):
        super().__init__(src, dst)
        self.voltage = voltage

    def add_to_graph(self, graph):
        graph.add_edge(self.src, self.dst, type='Vsource', voltage=self.voltage)
