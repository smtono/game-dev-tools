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

Each object also has a context that can be used to store information about the object, that is defined by the developer.
This can contain any relevant information that may change the flow of dialogue, 
such as the player's inventory or the current location, or relationship with NPCs.

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
class Action:
    """
    This class is used to store the information for an Action
    
    Actions are either a response to a dialogue or a piece of dialogue
    that continues the current dialogue
    
    TODO: add more here
    """
    ctx: dict
    action_id: int
    dialogue_id: int
    next_id: int

@dataclass(frozen=True)
class Dialogue:
    """
    This class is used to store the information for a Dialogue.
    
    A dialogue is a "node" in the tree
    
    Data:
        dialogue_id: int
            Used for identifying the dialogue
        text: str
            Used for storing the text of the dialogue
        actions: list
            Used for storing the replies to the dialogue
    """
    ctx: dict
    dialogue_id: int
    text: str
    actions: list[Action]

class Scene:
    """
    This class is used to store the information for a Scene.
    
    A scene is a "block" in the tree in which dialogue goes in a cycle
    
    Data:
        scene_id: int
            Used for identifying the scene
        dialogue_id: int
            Used for identifying the starting dialogue
        is_connected: bool
            Used to determine if the scene is connected to another scene
    """

    def __init__(self, ctx: dict, scene_id: int, dialogue_id: int) -> None:
        self.ctx = ctx
        self.scene_id = scene_id
        self.dialogue_id = dialogue_id

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
    
    def __init__(self, root: Scene) -> None:
        self.scenes = []
        self.dialogues = []
        self.actions = []

    def traverse(self, dialogue_id: int) -> Dialogue:
        """
        This function is used to traverse the tree and find the dialogue
        that corresponds with the dialogue_id
        
        Args:
            dialogue_id: int
                The ID of the dialogue to find
        Returns:
            Dialogue: The dialogue that corresponds with the dialogue_id
        """
        for dialogue in self.dialogues:
            if dialogue.dialogue_id == dialogue_id:
                return dialogue
        return None

    def add_scene(self, scene: Scene) -> None:
        """
        This function is used to add a scene to the tree
        
        Args:
            scene: Scene
                The scene to add to the tree
        """
        self.scenes.append(scene)
