"""
This module serves as the class definition for the Create class.\

Usage:
    create type [id]
"""

import os

import admin_dev_tools.dialogue_builder.cli.util.dialogue_cli_util as util
from admin_dev_tools.dialogue_builder.cli.commands.command import Command

# TODO:
# Make it so it makes a generic NPC with bare bones info
# Then use modify command to directly edit NPC
# Can ask user if they want to proceed with modifying their NPC
class Create(Command):
    """
    This is the class definition for the Create command in the dialogue CLI

    Attributes:
        name: str
            The name of the command
        args: list
            A list of possible arguments for the command

    Functions:
        syntax_check(args: list) -> bool
            Checks if the arguments are valid, raises errors if not
        create_npc() -> dict
            Creates a new NPC object
        execute() -> None
            Executes the command
    """

    def __init__(self, args: list):
        super().__init__()
        self.name = "create"
        self.description = "Create a new instance of NPC or scene."
        self.usage = "create type [id]"
        self.args = args
        
        # TODO: read in current npc data and store in npc_data

    def syntax_check(self, args: list) -> bool:
        """
        Checks if the arguments are valid, raises errors if not

        Args:
            args: list
                The arguments to check
        Returns:
            True if the arguments are valid, False otherwise
        """
        types = ["npc", "scene"]

        if len(args) == 0:
            print("Error: No arguments provided.")
            return False
        if len(args) > 2:
            print("Error: Too many arguments provided.")
            return False
        if args[0] not in types:
            print(f"Error: {args[0]} Type does not exist.")
            return False
        if len(args) == 2:
            # check if id is valid
            pass
        return True

    def execute(self, args: list) -> dict:
        """
        This function executes the command

        Args:
            args: list
                The arguments to pass to the command
        Returns:
            The created NPC or scene
        """
        os.system('cls')

        if args[0] == "npc":
            return self.create_npc()
        if args[0] == "scene":
            npc_id = "0000"
        while npc_id not in npc_data:
            print("Please enter the NPC ID that this scene is associated with")
            npc_id = util.prompt_id()
            if npc_id in npc_data:
                scene = self.create_scene(npc_id)
                break
            print("This NPC does not exist")
            print("Trying again. . .")

    # Utility functions
    def create_scene(self, npc_id: str) -> dict:
        """
        Creates a new instance of a scene in regard to a particular NPC

        Args:
            npc_id: str
                The ID of the NPC that is associated with this scene
        Returns:
            A dictionary of the scene object
        """
        scene = {
            "npc_id": "",
            "trigger": "",
            "scene_id": "",
            "dialogues": []
        }

        print(f"Creating a new scene for NPC {npc_id}")
        scene['npc_id'] = npc_id

        # Trigger Event
        scene['trigger'] = util.prompt_string("Please enter the trigger event name "
                                "(ex. quest_name_begin, confidant_event_1, etc.)", False)

        scene_id = util.prompt_string("Please enter the scene ID "
                                "or nothing for automatic assignment", True)
        # Scene ID
        if scene_id:
            scene['scene_id'] = scene_id
        else:
            print("Generating ID automatically. . .")
            # create random 4 digit ID

        # Dialogues
        print("\nNow beginning dialogue tree creation")
        accept = input("Continue? (y/n): ")
        if accept == 'y':
            print("Now starting dialogue tree creation. . .")
            self.create_tree(npc_id)
        else:
            print("You can create a dialogue tree at any time")
            print("Adding scene data. . .")
            # Check for successful dialogue creation

        return scene

    def create_npc(self) -> dict:
        """
        Creates a new instance of an NPC

        Args:
            None
        Returns:
            A dict containing information on the new NPC
        """
        npc = {
            "id": "",
            "name": "",
            "portrait": "",
            "type": "",
            "mood": "",
            "actions": {
                "START_SESSION": {
                    "good": [
                        ""
                    ],
                    "neutral": [
                        ""
                    ],
                    "bad": [
                        ""
                    ]
                },
                "END_SESSION": {
                    "good": [
                        ""
                    ],
                    "neutral": [
                        ""
                    ],
                    "bad": [
                        ""
                    ]
                }
            },
        }
        print("Creating a new NPC")

        # ID
        while True:
            npc_id = util.prompt_id()
            if npc_id:
                npc['id'] = npc_id
            else:
                npc_id = util.find_next_id(npc_data)
                print(f"Creating an NPC with ID '{npc_id}'")
                break

        # Name
        npc['name'] = util.prompt_string("Please enter the NPC's name", False)

        # Portrait
        # Type
        npc_types = ['generic', 'quest_giver', 'shopkeeper', 'enemy']
        while True:
            npc_type = util.prompt_string(
                "Please enter the NPC's type. For a list of types enter 'types'",
                False
            )
            if npc_type == 'types':
                print("NPC Types:")
                print("\t", npc_types)
            elif npc_type in npc_types:
                npc['type'] = npc_type
                break
            else:
                print(f"Input '{npc_type}' is not a valid type. Trying again. . .")

        # Mood
        while True:
            print(
                "\nPlease enter the starting integer for the mood of this NPC, from -10 to 10"
                "\nPositive integers means positive mood, "
                "negative means a starting negative mood:"
            )
            npc_mood = util.prompt_number(False)
            if float(npc_mood) > 10 or float(npc_mood) < -10:
                print("Input must be between -10 and 10. Trying again. . .")
            else:
                npc['mood'] = npc_mood
                break

        # Actions
        print("\nNow adding dialogue actions to this NPC. . .")
        actions = self.add_actions()

        # Scenes
        print("\nNow adding dialogue trees to this NPC. . .")
        scenes = self.create_scene(npc_id)

        print("Now exiting NPC creation. . .")
        return npc

    def create_tree(self, npc_id: str) -> dict:
        """
        Creates a new instance of a dialogue tree in regard to a particular scene

        Args:
            None
        Returns:
            A dictionary containing dialogue tree data
        """
        dialogue_tree = {
            "npc_id": npc_id,
            "branches": [

            ]
        }

        creating = True
        branch_num = 0
        while creating:
            current_branch = {
                "dialogue_id": {
                    "text": "",
                    "options": []
                },
            }
            # Dialogue ID
            dialogue_id = util.prompt_string("Please enter an ID for this dialogue prompt, "
                                "or nothing for automatic assignment", True)

            if dialogue_id:
                current_branch[dialogue_id] = current_branch.pop('dialogue_id')
            else:
                print("Generating ID automatically. . .")
                # create ID automatically by finding the highest ID and adding 1
                dialogue_id = util.find_next_id(npc_data[npc_id]['scenes'])
                current_branch[dialogue_id] = current_branch.pop('dialogue_id')

            # Dialogue prompt
            current_branch[dialogue_id]['text'] = \
                util.prompt_string("Please enter the the prompt for this dialogue:\n", False)

            # Dialogue options
            print("Now beginning option creation. . .")
            print("How many dialogue choices will there be for this prompt?\n"
                "Please note that additional prompts may be necessary for each option.")
            num = util.prompt_number(False)

            for i in range(int(num)):
                while user_input == 'ids':
                    text = util.prompt_string(f"Please input the text for option #{i + 1}", False)
                    user_input = util.prompt_string(
                        f"Please input the ID of the next dialogue prompt for option #{i + 1}, "
                        "or enter 'ids' for a list of prompts and their ids", False
                    )

                    for dialogue_id, prompt in npc_data[npc_id]['scenes'].items():
                        print(f"{dialogue_id}: {prompt['text']}")

                next_dialogue_id = user_input

                # Add to current branch
                current_branch[dialogue_id]['options'].append(
                    {
                        'text': text,
                        'next_dialogue_id': next_dialogue_id
                    }
                )

                # Check if correct, break if done
                again = util.prompt_confirm("\n" + current_branch + "\n")
                if not again:
                    creating = False

            dialogue_tree['branches'].append(current_branch)
            branch_num += 1

            # Clear branch for new one
            current_branch.clear()

            # Continue to branch off each option
                # Ask if new branch needs to be created

        return dialogue_tree
