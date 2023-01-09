"""
This is used to test dialogue functionality in the command line
NPCs will have their own dialogue trees, user will make choices to navigate through these trees
"""

# TODO: incorporate DialogueSet and DialogueOption into this, it will be cleaner
# For now just have linear navigation through directly with dictionaries

def start(npc: dict=None):
    """
    Starts the dialogue with the NPC

    Args:
        npc: dict
            The NPC to start the dialogue with
    Returns:
        None
    Raises:
        None
    """
    if npc:
        # find this npc in the data file
        pass
    else:
        # do generic talk
        pass

if __name__ == '__main__':
    pass
