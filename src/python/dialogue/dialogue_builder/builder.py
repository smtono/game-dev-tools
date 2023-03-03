"""
Build a dialogue tree using a script written by the user

This file contains functions that assist in tokenizing, parsing, and
adding semantics to user scripts to aid in the creation of dialogue trees.

The following functions are provided:

"""

import os

def parse(filename: str) -> list[str]:
    """
    Breaks up a user script into individual tokens
    
    Args:
        filename (str)
            The name of the user script to be parsed
    Returns:
        List of parsed tokens
    """
    with open(filename, 'r') as f:
        script = f.read()
    return script.split()

def tokenize(tokens: list[str]) -> list[tuple[str, str]]:
    """
    Assigns tokens to each part of script
    These tokens are then used to create a tree

    Args:
        tokens (list[str])
            A list of user script tokens
    Returns:
        A list of tuples of the form (token, part of script)
    Raises:
        SyntaxError: if the script is malformed
    """
    # TODO: decide script syntax
    token_types = []
    tokens = []

def interpret(tokens: list[tuple[str, str]]) -> list[str]:
    """
    Interprets the tokens and returns the result
    """

