"""
This module servers as a helper to reading in scripts for the dialogue system.
Users can write their own scripts containing NPC data and dialogues, which is parsed by this module.

Scripts are set up in the following manner:
    a tag at the top includes the type of script, (NPC, Item, etc.)
    then a keyword "begin" is used to start the script
    data for the NPC is then written in the following format:
        name: the name of the NPC
        portrait: the name of the portrait image
        type: the type of NPC (e.g. "merchant", "guard", etc.)
        mood: the starting integer of the NPC's mood
    dialogues are then written in the following format:
"""
# TODO: parse portrait file to get image
# TODO: add way to randomly generate data
import prototypes.game_objects.npc as npc

import os
import pygame

def parse_image(image_name: str) -> pygame.Surface:
    """
    Parses an image from the image directory.

    Args:
        image_name: the name of the image to parse
    Returns:
        The image as a pygame.Surface
    """
    pygame.image.load(f'/../portraits/{image_name}')

def parse_npc(args: list):
    """
    Parses the NPC data.

    Args:
        args: the arguments to parse
    Returns:
        None
    """
    # Get the name
    name = args[0].strip()

    # Get the portrait
    portrait = args[1].strip()

    # Get the type
    npc_type = args[2].strip()

    # Get the mood
    mood = args[3].strip()

    # Create the NPC
    npc = npc.NPC(name, portrait, npc_type, mood)

    # Add the NPC to the NPC list
    npc_list.append(npc)

def parse_enemy(args: list):
    pass

# TODO: maybe make generic and input file to be read?
def parse(lines: list) -> dict:
    """
    Reads and parses the script into usable data.

    Args:
        file: str
            The path to the file to read
    Returns:
        A dict with parsed NPC data
    """
    result = {}
    # Open the file
    
    # Push lines into a list
    script_data = []

    # Go through each line, parse for type
    
    return result
    

if __name__ == "__main__":
    parse(os.path.join(os.getcwd(), "data", "example_script.txt"))
