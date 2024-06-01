"""Module providing an example of class docstream"""


class Person:  # pylint: disable=too-few-public-methods
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name: str, surname: str, age: int):
        """_summary_

        Args:
            name (str): _description_
            surname (str): _description_
            age (int): _description_
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """_summary_

        Args:
            additional (str, optional): _description_. Defaults to "".
        """

        print(
            f"My name is {self.name} {self.surname}. I am {self.age} years old."
            + additional
        )  # noqa: E501, E261
