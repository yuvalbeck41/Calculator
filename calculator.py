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
        """
        This method runs the calculator, and presents the UI to the user
        """
        print("*" * 40)
        print("* Welcome to our super calculator")
        print("* In order to exit type exit")
        print("* The currently supported operations:")
        # Here we print all of the supported operators
        for operat in self.operators:
            print("*", operat.get_symbol())
        # If we don't have any operators we wish to exit
        if len(self.operators) == 0:
            print("* We don't support any operators yet")
            exit()
        print("*" * 40)
        while True:
            inp = input(PADDING + " ")
            if inp == "exit":
                break
            # We get our input and then we match it to the regex expression
            group = patt.match(inp)
            if group is None:
                print(PADDING, "Please follow the syntax: <number><operation><number>")
                continue
            # We check to see if the operator we were given is supported
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
            # If  it is supported we will print out the result
            print(PADDING, operation.act(x, y))
        print("Good bye")

