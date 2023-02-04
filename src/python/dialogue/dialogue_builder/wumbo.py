"""
This module is used to store units for Scenes and Dialogues.

A more rigorous overview is as follows:

SCENE Objects:
Scene ID
- This is how we know what to show the user and decide what the starting dialogue should be
Starting Dialogue ID
- This will lead to the first Dialogue which then leads to a Reply

DIALOGUE Objects:
Dialogue ID
- This is what corresponds with an NPC object
Text
- This is the actual words associated with the piece of dialogue
Options for responses (OPTIONAL)
- These are pieces of text that the USER chooses in response to the Dialogue
- These are known as "REPLIES"

REPLY Objects:
Reply ID
- This corresponds to the specific reply in a Dialogue
Dialogue ID
- Leads back to the dialogue choice that came with this Reply object
NEXT ID
- Leads to the NEXT Dialogue object

These objects, specifically the Dialogue and Reply objects, are used to create a link between each other.
We can then chain these links together to create a "tree" of dialogue options.
"""

from dataclasses import dataclass

"""
Data Class definitions

These data classes are used to store the information for each object
These objects are:
- Tree
- Scene
- Dialogue
- Reply

These objects work together to form a tree of dialogue options
"""
# TODO: consider linked list implementation
# TODO: clean up how these objects interact with each other
@dataclass(frozen=True)
class Tree:
    """
    This class is used to store the information for a Tree.
    """
    root: int # Dialogue ID
    scenes: list

@dataclass(frozen=True)
class Scene:
    """
    This class is used to store the information for a Scene.
    
    A scene is a "block" in the tree in which dialogue goes in a cycle
    A scene completes at the end of this block
    """
    scene_id: int
    dialogue_id: int

@dataclass(frozen=True)
class Dialogue:
    """
    This class is used to store the information for a Dialogue.
    
    A dialogue is a "node" in the tree
    """
    dialogue_id: int
    text: str
    replies: list

@dataclass(frozen=True)
class Reply:
    """
    This class is used to store the information for a Reply.
    
    Replies are attached to Dialogue objects and
    are what the user interacts with to progress the scene
    """
    reply_id: int
    dialogue_id: int
    next_id: int

"""
Function Definitions
"""
# TODO: tree traversal
#    - BFS
#    - DFS
# These are for searching for specific dialogue nodes
