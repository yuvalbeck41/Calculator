from operators import operator


@operator.Operator.register_operator
class Subtraction(operator.Operator):
    """
        The subtraction operator, this operator allows us to subtraction one number from the other
    """
    def __init__(self):
        super().__init__('-')

    def act(self, x: int, y: int) -> int:
        return x - y
