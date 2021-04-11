from operators.operator import Operator
import re
import os

# Adding the regex pattern to find the operators
patt = re.compile(r"(\d+)[ \t]*([^\w\s])[ \t]*(\d+)")
PADDING = ">"
# The following code loads all the operators dynamically, this is kind of a bad practice but I had to add it for your
# exercise
for module in os.listdir(os.path.join(os.path.dirname(__file__), 'operators')):
    if module in ['__init__.py', 'calculator.py', 'operator.py'] or module[-3:] != '.py':
        continue
    __import__(f"operators.{module[:-3]}", locals(), globals())
del module


class Calculator:
    """
        The calculator class, this class runs the entire calculator
    """
    def __init__(self):
        self.operators = Operator.get_registered_operators()

    def run(self):
        print("*" * 40)
        print("* Welcome to our super calculator")
        print("* In order to exit type exit")
        print("* The currently supported operations:")
        for operat in self.operators:
            print("*", operat.get_symbol())
        if len(self.operators) == 0:
            print("* We don't support any operators yet")
            exit()
        print("*" * 40)
        while True:
            inp = input(PADDING + " ")
            if inp == "exit":
                break
            group = patt.match(inp)
            if group is None:
                print(PADDING, "Please follow the syntax: <number><operation><number>")
                continue
            operator = group.group(2)
            operation = None
            for operat in self.operators:
                if operat.get_symbol() == operator:
                    operation = operat
                    break
            if operation is None:
                print(PADDING, "Unsupported operator")
                continue
            x = int(group.group(1))
            y = int(group.group(3))
            print(PADDING, operation.act(x, y))
        print("Good bye")

