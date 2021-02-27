from component import Component


class NOT(Component):
    def __init__(self, n_inputs, n_outputs):
        super().__init__(n_inputs, n_outputs)

    def action(self, inputs):
        return not inputs[0]


class OR(Component):
    def __init__(self, n_inputs, n_outputs):
        super().__init__(n_inputs, n_outputs)

    def action(self, inputs):
        for i in inputs:
            if i == True:
                return 1
        return 0
