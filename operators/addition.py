from operators import operator


@operator.Operator.register_operator
class Addition(operator.Operator):
    def __init__(self):
        super().__init__('+')

    def act(self, x: int, y: int) -> int:
        return x + y