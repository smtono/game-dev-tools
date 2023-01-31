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

class Scene:
    """
    This class is used to store the information for a Scene.
    """
    def __init__(self, scene_id, dialogue_id):
        self.scene_id = scene_id
        self.dialogue_id = dialogue_id

class Dialogue:
    """
    This class is used to store the information for a Dialogue.
    """
    def __init__(self, dialogue_id, text, replies):
        self.dialogue_id = dialogue_id
        self.text = text
        self.replies = replies

class Reply:
    """
    This class is used to store the information for a Reply.
    """
    def __init__(self, reply_id, dialogue_id, next_id):
        self.reply_id = reply_id
        self.dialogue_id = dialogue_id
        self.next_id = next_id
        
# TODO: methods for loading and saving the data
