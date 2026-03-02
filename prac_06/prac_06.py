"""
Write a Monster class definition.
A Monster knows: name (str), number_of_teeth (int) and colour (str).
Use default values: "Mike, 0 and "blue" for these three attributes respectively.
Write a method called is_scarry.
A Monster is scarry if it has more than 16 teeth or is red.
Include docstrings for your class and methods.
"""

class Monster:

    def __init__(self, name: str = "Mike", number_of_teeth: int = 0, colour: str = "Blue"):
        """
        Initialize a Monster instance.
        name (str): The monster's name. Defaults to "Mike".
        number_of_teeth (int): The number of teeth the monster has. Defaults to 0.
        colour (str): The colour of the monster. Defaults to "blue".
        """
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def is_scary(self) -> bool:
        """
        Determine whether the monster is scary.

        A monster is considered scary if:
        - It has more than 16 teeth OR
        - Its colour is red.

        Returns:
            bool: True if the monster is scary, False otherwise.
        """
        return self.number_of_teeth > 16 or self.colour.lower() == "red"

