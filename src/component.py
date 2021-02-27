class Component:
    def __init__(self, n_inputs, n_outputs):
        self.inputs = [0 for i in range(n_inputs)]
        self.outputs = [0 for i in range(n_outputs)]

    def action(self, inputs):
        return inputs

    def update(self):
        next_state = self.action(self.inputs)
        if not isinstance(next_state, list):
            next_state = [next_state]

        self.outputs = next_state

    def __repr__(self):
        inputs = ' '.join(['1' if i else '0' for i in self.inputs])
        outputs = ' '.join(['1' if o else '0' for o in self.outputs])
        return f'[{inputs}] [{outputs}]'
