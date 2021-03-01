from .component import Component


class Connection:
    def __init__(self, id0, pin0, id1, pin1):
        self.id0 = id0
        self.pin0 = pin0
        self.id1 = id1
        self.pin1 = pin1
        self.old_value = 0
        self.value = 0

    def compare(self):
        return self.old_value == self.value

    def __repr__(self):
        return f'[{self.id0} {self.id1} {self.value} {self.old_value}]'


class Board(Component):
    def __init__(self, n_inputs, n_outputs):
        super().__init__(n_inputs, n_outputs)
        self.components = []
        self.connections = []

    def add_component(self, c):
        self.components.append(c)
        return len(self.components) - 1

    def connect(self, id0, pin0, id1, pin1):
        connection = Connection(id0, pin0, id1, pin1)
        self.connections.append(connection)

    def action(self, inputs):
        for i, component in enumerate(self.components):
            component.update()
            for c in self.connections:
                if c.id0 == i:
                    c.value = component.outputs[c.pin0]

        for c in self.connections:
            if c.id0 == -1:
                c.value = inputs[c.pin0]

        while True:
            to_update = [i for i, c in enumerate(
                self.connections) if c.id1 != -1 if not c.compare()]

            if to_update == []:
                break

            for i in to_update:
                conn = self.connections[i]
                id1 = conn.id1
                pin1 = conn.pin1

                self.components[id1].inputs[pin1] = conn.value
                conn.old_value = conn.value
                self.components[id1].update()

                for c in self.connections:
                    if c.id0 == id1:
                        for i, o in enumerate(self.components[id1].outputs):
                            if c.pin0 == i:
                                c.value = o

        return [c.value for c in self.connections if c.id1 == -1]
