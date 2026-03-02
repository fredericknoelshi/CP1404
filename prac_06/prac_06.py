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

"""
Write a user class, for a fun Taco Reward program. 
A User knows: name, number of tacos (starts at 5, goes down when they give a taco), and score 
A User can give a taco to another user 
We should be able to print a User like: Ben, 2 points, 4 tacos left 
When we make a user, they start with the name we want and appropriate default values
"""

class User:
    """
    Class representing a user in a taco reward program
    """
    def __init__(self, name: str, number_of_tacos: int = 0, score: int = 0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def give_taco(self, other_user: "User"):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += self.score
        else:
            print(f"{self.name} has no tacos left to give.")

    def __str__(self) -> str:
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"