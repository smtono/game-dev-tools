"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

import os
import admin_dev_tools.dialogue_builder.cli.util.dialogue_cli_util as util

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

# Check data exists
if os.path.isfile(os.path.join(__location__, 'data', 'npc_data.json')):
    print("NPC data found\n")
    # Read data
    npc_data = util.read_npc_data()
else:
    print("NPC data not found\n")
    print("A new NPC data file will be created once data has been entered\n")


def add_actions() -> dict:
    """
    Adds inital dialgoue for an NPC
    An action is comprised of a dialogue context, dialogue types,
    and then the actual text associated with each type.

    context:
        This is the reason for the dialogue to be said.
        It can be something like starting a new conversation, ending one,
        being involved with a ceratin quest, etc.
    type:
        This is more specific dialogue to be said depending on
        the relationship of the player to the NPC, or if certain
        requirements have been met to warrant a specific dialogue
        snippet to be said
    test:
        This is the actual content of a dialogue point

    Args:
        None
    Returns:
        A dict of inital dialogue points for the NPC
    """
    actions = {}

    print("\nNow beginning action dialogue creation. . .")
    print("\nAn action dialogue is said at the beginning "
          "and end of sessions when chatting with NPCs.")
    print("\nThese dialogues can be generic or tied to confidant events, quests, etc.")

    print("Please enter the context for this dialogue ex. "
        "START_SESSION, END_SESSION, CONFIDANT_1 etc"
        "\nOr enter 'help' for more information.")
    dialogue_context = util.prompt_string("\nInput now: ", False)
    while dialogue_context == 'help':
        print("context:"
        "\nThis is the reason for the dialogue to be said."
        "\nIt can be something like starting a new conversation, ending one,"
        "\nbeing involved with a ceratin quest, etc.")
        dialogue_context = util.prompt_string("\nInput context now: ", False)

    print("Please enter the number of types for this context, or type 0 for more information")
    num = util.prompt_number(False)
    while num == "0":
        print("type:"
        "\nThis is more specific dialogue to be said depending on"
        "\nthe relationship of the player to the NPC, or if certain"
        "\nrequirements have been met to warrant a specific dialogue"
        "\nsnippet to be said")
        print("Please enter the number of types")
        num = util.prompt_number(False)

    dialouge_types = []
    for i in range(int(num)):
        dialogue_type = util.prompt_string(
            f"Please enter the type for this dialouge {i} i.e. "
            "the reason for this dialogue to be said ex. GOOD, BAD, QUEST_1_IN_PROGRESS, etc"
            "\nInput now: ",
            False)
        dialouge_types.append(dialogue_type)

    # Add text
    return actions

def read_command(user_input: str):
    """
    Reads command passed in by user for the CLI,
    passes to correct function based on it

    Args:
        command: str
            The command passed in by the user
    Returns:
        None
    """
    cmd_parts = user_input.split(" ")
    command = cmd_parts[0]
    cmd_args = cmd_parts[1:]

    supported_commands = ['create', 'modify', 'delete']

    if command == 'help':
        print("This is a CLI that allows you to create or modify NPCs or Scenes \
                    for dialogue prompts in the story parts of Purgatory.\n\n \
                    Here's a list of commands you can use to get started:\n \
                        create \
                        modify \
                        delete \
                    Type 'help' after these commands for more information.")
    elif command in supported_commands:
        if command == 'create':
            create(cmd_args)
        elif command == 'modify':
            modify(cmd_args)
        elif command == 'delete':
            delete(cmd_args)
    elif not cmd_args:
        print("Please provide arguments for this command, or type 'help'")

def dialogue_cli():
    """
    The command line interface for creating, modifying, and deleting NPC data

    Args:
        None
    Returns:
        None
    """
    # Welcome
    print("Welcome to the NPC Chat Builder CLI!")
    print("Type 'help' for a list of commands.")

    # Wait for command
    while True:
        command = input(">>> ")
        if command == "help":
            print("Here's a list of commands you can use to get started:",
                  "\n\tcreate\n\tmodify\n\tdelete\n\thelp\n",
                  "Type 'help' after any command for additional info")
        elif command == 'exit':
            print("Now exiting NPC Chat Builder CLI. . .")
            # Cleanup
            return
        else:
            read_command(command)

if __name__ == '__main__':
    dialogue_cli()
