from src.gate import NOT, OR
from src.board import Board


def NOR(n_inputs, n_outputs):
    b = Board(n_inputs, n_outputs)
    c0 = b.add_component(OR(2, 1))
    c1 = b.add_component(NOT(1, 1))
    b.connect(-1, 0, c0, 0)
    b.connect(-1, 1, c0, 1)
    b.connect(c0, 0, c1, 0)
    b.connect(c1, 0, -1, 0)

    return b


def table(gate, table_in):
    table_out = []
    for i in table_in:
        gate.inputs = i
        gate.update()
        table_out.append(gate.outputs)
    return table_out


def test_not():
    table_in = [
        [0], [1]
    ]

    table_out = [
        [1], [0]
    ]

    gate = NOT(1, 1)
    assert table(gate, table_in) == table_out


def test_or():
    table_in = [
        [0, 0], [0, 1], [1, 0], [1, 1]
    ]

    table_out = [
        [0], [1], [1], [1]
    ]

    gate = OR(2, 1)
    assert table(gate, table_in) == table_out


def test_nor():
    table_in = [
        [0, 0], [0, 1], [1, 0], [1, 1]
    ]

    table_out = [
        [1], [0], [0], [0]
    ]

    assert table(NOR(2, 1), table_in) == table_out


def test_and_nor():
    table_in = [
        [0, 0], [0, 1], [1, 0], [1, 1]
    ]

    table_out = [
        [0], [0], [0], [1]
    ]

    b = Board(2, 1)
    c0 = b.add_component(NOR(2, 1))
    c1 = b.add_component(NOR(2, 1))
    c2 = b.add_component(NOR(2, 1))
    b.connect(-1, 0, c0, 0)
    b.connect(-1, 0, c0, 1)
    b.connect(-1, 1, c1, 0)
    b.connect(-1, 1, c1, 1)
    b.connect(c0, 0, c2, 0)
    b.connect(c1, 0, c2, 1)
    b.connect(c2, 0, -1, 0)

    assert table(b, table_in) == table_out
