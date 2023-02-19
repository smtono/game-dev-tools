"""
This module serves as the class definition for the Command class.
The Command class is an abstract class that is meant to be inherited by
CLI commands. It contains the basic methods that all commands should have.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    This is the class definition for a generic Command

    Attributes:
        name: str
            The name of the command
        args: list
            A list of possible arguments for the command

    Functions:
        syntax_check(args: list) -> bool
            Checks if the arguments are valid, raises errors if not
        execute() -> None 
            Executes the command
    """
    def __init__(self):
        """
        The constructor for the Command class
        """
        self.name = ""
        self.description = ""
        self.usage = ""
        self.args = []

    def get_help(self) -> str:
        """
        Returns the help message for the command
        """
        return f"Usage: {self.usage}: {self.description}"

    @abstractmethod
    def syntax_check(self, args: list) -> bool:
        """
        Checks if the arguments are valid, raises errors if not

        Args:
            args: list
                The arguments to check
        Returns:
            True if the arguments are valid, False otherwise
        """

    @abstractmethod
    def execute(self, args: list):
        """
        This function executes the command

        Args:
            args: list
                The arguments to pass to the command
        """
