class calculator:
    """A simple calculator class to perform operations on a list of numbers."""

    def __init__(self, lists: list) -> None:
        """Initialize the calculator with a list of numbers."""
        if not isinstance(lists, list):
            raise TypeError("Input must be a list")
        if not all(isinstance(x, (int, float)) for x in lists):
            raise TypeError("All elements in the list must be int or float")
        self.list = lists

    def __add__(self, objects) -> None:
        """Add an integer or float to each element in the list."""
        if isinstance(objects, (int, float)):
            self.list = [x + objects for x in self.list]
            print(self.list)
        else:
            raise TypeError("Operand must be an int or float")

    def __mul__(self, objects) -> None:
        """Multiply each element in the list by an integer or float."""
        if isinstance(objects, (int, float)):
            self.list = [x * objects for x in self.list]
            print(self.list)
        else:
            raise TypeError("Operand must be an int or float")

    def __sub__(self, objects) -> None:
        """Subtract an integer or float from each element in the list."""
        if isinstance(objects, (int, float)):
            self.list = [x - objects for x in self.list]
            print(self.list)
        else:
            raise TypeError("Operand must be an int or float")

    def __truediv__(self, objects) -> None:
        """Divide each element in the list by an integer or float."""
        if isinstance(objects, (int, float)):
            if objects == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            self.list = [x / objects for x in self.list]
            print(self.list)
        else:
            raise TypeError("Operand must be an int or float")
