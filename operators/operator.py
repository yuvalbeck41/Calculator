class Operator:
    """This is the operators class it allows to you to create new operators for the calculator"""
    _available_operators = []

    def __init__(self, symbol: str):
        """
        Each operators has a symbol the represents it
        :param symbol:
        """
        if len(symbol) != 1:
            raise SyntaxError("Symbol must be 1 char long")
        self.symbol = symbol

    def get_symbol(self) -> str:
        """
        :return: the operators symbol
        """
        return self.symbol

    def act(self, x: int, y: int) -> int:
        """
        This functions acts on two ints
        :param x: the first int
        :param y: the second int
        :return: the result of operators(x, y)
        """
        raise NotImplementedError("Please Implement this method")

    @classmethod
    def _register_operator(cls, operator):
        """
        This function registers a new operators, this function should only be used internally
        :param operator: the initialized operators
        """
        if not isinstance(operator, Operator):
            raise TypeError
        cls._available_operators.append(operator)

    @classmethod
    def register_operator(cls, operator):
        """
        This decorator registers a new operators class
        :param operator: the class
        :return:
        """
        cls._register_operator(operator())
        return operator

    @classmethod
    def get_registered_operators(cls):
        """
        :return: All of the registered operators
        """
        return cls._available_operators