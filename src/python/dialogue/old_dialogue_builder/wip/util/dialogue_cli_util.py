"""
This module is meant to aid in file reading and manipulation
for the Dialogue CLI, along with other helpful methods that
do not fit in any other module.
"""

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

def read_npc_data() -> dict:
    """
    Reads the currently used file for storing NPC data and returns it as a dict

    Args:
        None
    Returns:
        The dict of NPC data
    """
    path = os.path.join(__location__, "data", "npc_data.json")
    with open(path, "r", encoding="UTF-8") as data:
        return json.load(data)

def write_npc_data(npc_data: dict, new_npc: dict) -> None:
    """
    Writes to the currently used file for storing NPC data

    Args:
        npc_data: dict
            The dict of NPC data
        new_npc: dict
            The dict of the new NPC to add to the NPC data
    Returns:
        None
    """
    # Append NPC to existing NPC data
    npc_data.update(new_npc)

    # Write to file
    path = os.path.join(__location__, "data", "npc_data.json")
    with open(path, "w", encoding="UTF-8") as data:
        json.dump(npc_data, data, indent=4)

def find_next_id(data: dict) -> str:
    """
    Finds the next available ID in the NPC data and returns it as a 4 digit string

    Args:
        npc_data: dict
            A dictionary of the current NPC data
    Returns:
        The next available ID as a string
    """
    # An ID is the key in the dict, so the length of the dict is the next available ID
    next_id = str(len(data))
    if len(next_id) < 4:
        next_id = next_id.zfill(4)
    return next_id

def prompt_confirm(user_input: str) -> bool:
    """
    Prompts user to confirm their input

    Args:
        user_input: str
            The input by the user
    Returns:
        Whether or not the user accepts the input
    """
    accept = input(f"Is '{user_input}' OK? (y/n) ")
    if accept in ('y', ''):
        print(f"Adding '{user_input}'. . .")
        return True
    print("Trying again. . .")
    return False

def prompt_string(input_prompt: str, null_allowed: bool) -> str:
    """
    Prompts the user for input and returns the input

    Args:
        input_prompt: str
            The prompt to display to the user
        null_allowed: bool
            Whether or not the user can input nothing
    Returns:
        The input from the user
    """
    while True:
        text = input("\n" + input_prompt + "\n>>> ")
        if text or null_allowed:
            return text
        else:
            print("No input detected. Trying again. . .")

def prompt_number(null_allowed: bool) -> str:
    """
    Prompts for a number and checks if numeric, prompts again if not

    Args:
        None
    Returns:
        Whether the input is numeric or not
    """
    while True:
        user_input = prompt_string("Enter the value now: ", null_allowed)
        if not user_input:
            return user_input
        try:
            float(user_input)
        except ValueError:
            print(f"Value '{user_input}' is not numeric. Trying again. . .")
            continue
        return user_input

def prompt_id() -> str:
    """
    Prompts for an ID input, then checks if it is formatted correctly,
    prompts again if not

    Args:
        None
    Returns:
        The correctly formatted ID
    """
    while True:
        print("Please enter a 4 digit ID or nothing for automatic assignment")
        user_input = prompt_number(True)
        if len(user_input) != 4:
            if user_input == '':
                break
            print("Incorrect length for ID. Trying again. . .")
        else:
            return user_input
