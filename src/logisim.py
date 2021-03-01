from .board import Board
from .gate import NOR

b = Board(2, 1)
b.add_component(NOR())
b.add_component(NOR())
b.add_component(NOR())

b.connect(-1, 0, 0, 0)
b.connect(-1, 0, 0, 1)
b.connect(-1, 1, 1, 0)
b.connect(-1, 1, 1, 1)
b.connect(0, 0, 2, 0)
b.connect(1, 0, 2, 1)
b.connect(2, 0, -1, 0)

b.inputs = [0, 1]
b.update()
print(b)
