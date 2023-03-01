"""
Build a dialogue tree using a script written by the user

This file contains functions that assist in tokenizing, parsing, and
adding semantics to user scripts to aid in the creation of dialogue trees.

The following functions are provided:

"""

def tokenize(filename: str) -> list[tuple[str, str]]:
    """
    Breaks up a user script into individual tokens
    Assigns tokens to each part of script
    These tokens are then used to create a tree

    Args:
        filename: string
            The path to the user script
    Returns:
        A list of tuples of the form (token, part of script)
    Raises:
        SyntaxError: if the script is malformed
    """


