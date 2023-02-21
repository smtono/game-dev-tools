"""
This script is used to aid in the creation of a Dialogue Tree.

For a more detailed explanation of a Dialogue Tree, see the README.md file in the dialogue_builder directory.

A Dialogue Tree is a tree structure that is used to store the dialogue for a game.
A dialogue tree is made up of scenes and dialogues.
Scenes are a block of dialogues that are connected to each other.
Dialogues are the nodes in the tree that store the text and replies.
"Replies" are stored as "Actions" which are used for players to choose from.
    There can also be a "no reply" action which is used for the player to continue to the next dialogue.

This script loops for user input to aid in the creation of a Dialogue Tree.
This structure will be saved in a JSON file, in the same directory as this script.
(Which can be extracted using Python libraries, or other tools for other languages)

The following attributes will be asked for:
Scene:
    Scene ID: int
        Used for identifying the scene

        Dialogue ID: int
            Used for identifying the dialogue
                Text: str
                    Used for storing the text of the dialogue

                Action ID: int
                    Used for identifying the action
                Reply: str
                    Used for storing the reply text
        Next Dialogue ID: int
            Used for identifying the next dialogue

Example of a Dialogue Tree:
Dialogue 1
    Reply 1
        Dialogue 2
    Reply 2
        Dialogue 3
Dialogue 2
    Reply 1
        Dialogue 4
    Reply 2

Example Usage:
    root = Scene(1, 1)
    tree = Tree(root)
    next_scene = tree.traverse(2)
"""

import os

