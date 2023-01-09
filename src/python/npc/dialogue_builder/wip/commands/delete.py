"""
This module serves as the class definition for the Create class.
"""
    
from admin_dev_tools.dialogue_builder.cli.commands.command import Command


class Delete(Command):
    """
    This is the class definition for the Create command in the dialogue CLI
    
    Attributes:
        name: str
            The name of the command
        args: list
            A list of possible arguments for the command

    Functions:
        syntax_check(args: list) -> bool
            Checks if the arguments are valid, raises errors if not
        execute() -> None 
            Executes the command
    """

    def __init__(self, args: list):
        super().__init__()
        self.name = "delete"
        self.args = args

    def syntax_check(self, args: list) -> bool:
        """
        Performs a syntax check on the arguments

        Parameters:
            args: list
                The arguments to check

        Returns:
            bool
                True if the arguments are valid, False if they are not
        """
        if len(args) == 2:
            return True
        else:
            return False
        
        # check if data file exists
        # check if game object exists

    def execute(self, args: list):
        """
        Executes the command

        Parameters:
            args: list
                The arguments to use

        Returns:
            None
        """
        # delete the game object

    def delete(self, args: list):
        """
        Deletes an instance of an NPC or scene

        Args:
            args: list
                the arguments passed to the command
        Returns:
            None
        """
        info = {
            "help": "deletes an instance of NPC or scene.\n \
            Args:\n\
                type: The type of the instance you want to delete (NPC or Scene)\n\
                npc_id: The ID of NPC or scene to delete",
            "args": ['type', 'npc_id']
        }

        if args[0] == 'help':
            print(info['help'])

        # check if the NPC or scene exists

        # delete that entry from dictionary
