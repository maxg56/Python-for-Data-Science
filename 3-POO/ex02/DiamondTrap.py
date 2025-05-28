from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """A King is a Baratheon and a Lannister, but not a Stark."""

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a King character with the provided first name.

        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character's life.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon-Lannister"
        self.eyes = "golden"
        self.hairs = "dark golden"

    def die(self):
        """Mark the character as not alive."""
        self.is_alive = False

    