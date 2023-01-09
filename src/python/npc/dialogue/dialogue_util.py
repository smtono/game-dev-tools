"""
something happens
- [chat]
    - response ->SELECT_RESPONSE: 48
        [different chat options for response 48]
            - response
                [ different chat options ]
                EXIT_CHAT -> "cya l8r alig8r"
"""
from enum import Enum
import pygame

class DialogueOption():
    """
    Represents a single dialogue choice with attributes pertaining to morality

    Attributes:
        text: string
            The actual dialogue in text
        position: int
            The position of this choice in the menu
        morality: int
            Represents whether the choice is good, neutral, or bad
        next_dialogue: int
            A pointer to the identifier of the next dialogue prompt

    Functions:

    """
    text = ""
    position = -1
    morality = 0
    next_dialogue = -1

    def __init__(self, text: str, position: int, morality: int, next_dialogue: int) -> None:
        """
        Initializes a Dialogue object with a set of text, position to be in the menu, and which Morality it coaligns with

        Args:
            text: str
                The text of this dialogue option
            position: int
                The position this option will appear in the screen
            morality: int
                The alignment of this choice, positive is good, negative is bad, 0 is neutral
            next_dialogue: int
                A pointer to the identifier of the next dialogue prompt
        Returns:
            None
        Raises:
            None
        """
        self.text = text
        self.position = position
        self.morality = morality
        self.next_dialogue = next_dialogue

class DialogueSet():
    """
    Represents a set of choices the user can make during a conversation with an NPC

    Attributes:
        choices: list[Dialogue]
            a list of dialogue options to choose from

    Functions:
    """
    identifier = 0000
    prompt = ""
    choices = []

    def __init__(self, identifier: int, prompt: str, choices: list[DialogueOption]) -> None:
        """
        Initizalizes a Dialogue Set object with a list of Dialogue objects

        Args:
            identifier: int
                The id associated with this dialogue scene
            prompt: str
                The text to begin this dialogue scene
            choices: list
                A list of however many Dialogue objects are associated with this set
        Returns:
            None
        Raises:
            None
        """
        self.identifier = identifier
        self.prompt = prompt
        self.choices = choices

class DialogueBox():
    """
    A window for text during a dialogue sequence, as well as dialogue options to appear in

    Attributes:
        window: pygame.Surface
            the window to display the dialogue in
        portrait: pygame.Surface
            the portrait to display on the left of the window
        dialoge: str
            the dialogue to display in the window
        options: list
            the dialogue options for the user to choose from

    Functions:
        display_dialogue(self, dialogue: str) -> None
            Displays the dialogue in the window
        display_choices(self, dialogue_set: DialogueSet) -> None
            Displays the dialogue options in the window
        determine_choice(self, dialogue_set: DialogueSet, choice: Dialogue) -> Dialogue
            Determines which choice the user made, then displays the next dialogue in the tree.
        draw_window() -> pygame.Surface
            Draws the current window to store in the screen
    """
    window = None
    portrait = None
    dialogue = ""
    options = []

    def __init__(self) -> None:
        """
        Initializes a DialogueBox object
        """

    def set_text(self, dialouge_set: DialogueSet):
        """
        Sets the text up for the next time the window is drawn

        Args:
            dialogue_set: DialogueSet
                The prompt and dialogue options available for the current screen
        Returns:
            None
        Raises:
            None
        """
        self.dialogue = dialouge_set.prompt
        self.options = dialouge_set.choices
    
    def display_dialogue(self, dialogue: str) -> None:
        """
        Displays the dialogue set to the user
        """
        self.dialogue = dialogue

    def display_choices(self, dialogue_set: DialogueSet) -> None:
        """
        Displays the choices the user can make

        Args:
            dialogue_set: DialogueSet
                The set of dialogue options to display
        Returns:
            None
        Raises:
            None
        """
        self.options = dialogue_set.choices

    def determine_choice(self, dialogue_set: DialogueSet, choice: DialogueOption) -> DialogueOption:
        """
        Determines which choice the user made, then changes to the next dialogue in the tree.

        Args:
            dialogue_set: DialogueSet
                The set of dialogue options to display
        Returns:
            Dialogue
                The choice the user made
        Raises:
            None
        """
        pass

    def draw_window(self) -> pygame.Surface:
        """
        Draws the current dialogue box to display to the user
        
        Args:
            None
        Returns:
            A pygame surface to draw to the game window
        Raises:
            None
        """
        # Parameters
        width = 600
        height = 100
        window = pygame.Surface((width, height))
        
        # Parts
        background = pygame.Surface
        portrait = None
        dialogue = self.dialogue
        options = self.options

        # Draw the dialogue box background
        
        # Add in the character portrait on the top left of the box
        
        # Add the character name to the right of the portrait
        
        # Add in the dialogue below the name
        
        # Add in dialogue options below the dialogue
        
        # Choose option, return
