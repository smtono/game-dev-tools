"""
This module is used to store units for Scenes and Dialogues.

A more rigorous overview is as follows:

SCENE Objects:
Scene ID
- This is how we know what to show the user and decide what the starting dialogue should be
Starting Dialogue ID
- This will lead to the first Dialogue which then leads to an Action onject

DIALOGUE Objects:
Dialogue ID
- This is what corresponds with an NPC object
Text
- This is the actual words associated with the piece of dialogue
Options for responses (OPTIONAL)
- These are pieces of text that the USER chooses in response to the Dialogue
- These are known as "REPLIES"

ACTION Objects:
Action ID
- This is what corresponds with a response or a piece of dialogue
Previous Dialogue ID
- Leads back to the dialogue choice that came with this Reply object
NEXT ID
- Leads to the NEXT Dialogue object
Special Attributes (Optional Metadata)
- Dictionary of unique features associated with the action object, defined by the developer


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
- Action

These objects work together to form a tree of dialogue options
"""
@dataclass(frozen=True)
class Tree:
    """
    This class is used to store the information for a Tree.
    Trees can be made up of scenes, or individual dialogue nodes
    
    For Scenes:
        Scenes trees are composed of every possible "scene" that could occur
        Scenes may be connected with each other, but they are not required to be

    For Dialogue:
        Dialogue trees are composed of every possible dialogue that could occur in a scene
        "Trees" in this instance are really just a list of dialogue nodes that compose a scene
    """
    root: int # Dialogue ID
    nodes: list # List of Scene or Dialogue objects
    
    # TODO: is this a good idea?

@dataclass(frozen=True)
class Scene:
    """
    This class is used to store the information for a Scene.
    
    A scene is a "block" in the tree in which dialogue goes in a cycle
    A scene completes at the end of this block
    
    Data:
        scene_id: int
            Used for identifying the scene
        dialogue_id: int
            Used for identifying the starting dialogue
        is_connected: bool
            Used to determine if the scene is connected to another scene
    """
    scene_id: int
    dialogue_id: int

@dataclass(frozen=True)
class Dialogue:
    """
    This class is used to store the information for a Dialogue.
    
    A dialogue is a "node" in the tree
    
    TODO: add more here
    """
    dialogue_id: int
    text: str
    replies: list

@dataclass(frozen=True)
class Action:
    """
    This class is used to store the information for an Action
    
    Actions are either a response to a dialogue or a piece of dialogue
    that continues the current dialogue
    
    TODO: add more here
    """
    action_id: int
    dialogue_id: int
    next_id: int

"""
Function Definitions
"""
# TODO: tree traversal
#    - BFS
#    - DFS
# These are for searching for specific dialogue nodes
