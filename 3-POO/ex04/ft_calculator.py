class calculator:
    """A simple calculator class to perform operations on a list of numbers."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot Product is: {result:.1f}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [x + y for x, y in zip(V1, V2)]
        print(f"ADD Vector is: {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")
