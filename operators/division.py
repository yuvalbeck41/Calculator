from operators import operator


@operator.Operator.register_operator
class Division(operator.Operator):
    """
        The division operator, this operator allows us to divide two numbers
    """
    def __init__(self):
        super().__init__('/')

    def act(self, x: int, y: int) -> int:
        return x / y