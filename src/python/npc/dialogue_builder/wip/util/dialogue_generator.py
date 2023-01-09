"""
This module is used for generating dialogue scripts for NPCs,
without having to manually write them.

The generator will create base entities based on type input by the user,
dialogue will be created after the base entities are created.

Dialogue can be produced manually or randomly
To create dialogue manually, the user will be prompted to input 
"""

import prototypes.game_objects.npc as npc
import prototypes.game_objects.game_object as game_object

def generate_generic_game_object(object_data: dict):
    """
    Generates a generic game object via dictionary

    Args:
        None
    Returns:
        A game object with dictionary values as kwargs
    """
    game_object = game_object.GameObject(object_data)
    return game_object

def generate_npc(number_of_npcs: int, npc_type: str):
    """
    Generates a new NPC with starting stats.

    Args:
        None
    Returns:
        A newly initalized NPC object
    """
    npc = npc.NPC()

    # TODO: create NPC based on type
    # Create number of NPCs based on input
