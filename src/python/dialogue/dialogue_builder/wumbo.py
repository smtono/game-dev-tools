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

@dataclass(frozen=True)
class Scene:
    """
    This class is used to store the information for a Scene.
    """
    scene_id: int
    dialogue_id: int

@dataclass(frozen=True)
class Dialogue:
    """
    This class is used to store the information for a Dialogue.
    """
    dialogue_id: int
    text: str
    replies: list

@dataclass(frozen=True)
class Reply:
    """
    This class is used to store the information for a Reply.
    """
    reply_id: int
    dialogue_id: int
    next_id: int
