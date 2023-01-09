"""
This module serves as the class definition for the Create class.
"""
    
from admin_dev_tools.dialogue_builder.cli.commands.command import Command


class Modify(Command):
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
        self.name = "modify"
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
    
    def execute(self, args: list):
        """
        Executes the command

        Parameters:
            args: list
                The arguments to use

        Returns:
            None
        """

    def modify_npc(npc: dict):
        """
        Modifies an existing NPC

        Args:
            npc: dict
                The NPC to modify
        Returns:
            None
        """
        print("Modifying NPC. . .")
        # prompt what attribute to modify via list
        print("Please enter the number attribute you would like to modify:\n")
        print(
            "1. ID\n"
            "2. Name\n"
            "3. Portrait\n"
            "4. Type\n"
            "5. Mood\n"
            "6. Actions\n"
            "7. Scenes\n"
        )
        while True:
            option = util.prompt_number(False)
            if option:
                break

        # TODO: make separate function, maybe can access dict by index, so use option to access it
        # ID
        if option == 1:
            while True:
                npc_id = util.prompt_id()
                if npc_id:
                    npc['id'] = npc_id
                    break
                print("ID cannot be empty. Trying again. . .")

        # Name
        elif option == 2:
            while True:
                npc_name = util.prompt_string("Please enter the NPC's name", False)
                if npc_name:
                    npc['name'] = npc_name
                    break
                print("Name cannot be empty. Trying again. . .")

        # Portrait
        elif option == 3:
            while True:
                npc_portrait = util.prompt_string("Please enter the NPC's portrait", False)
                if npc_portrait:
                    npc['portrait'] = npc_portrait
                    break
                print("Portrait cannot be empty. Trying again. . .")

        # Type
        elif option == 4:
            while True:
                npc_type = util.prompt_string("Please enter the NPC's type", False)
                if npc_type:
                    npc['type'] = npc_type
                    break
                print("Type cannot be empty. Trying again. . .")

        # Mood
        elif option == 5:
            while True:
                print(
                    "\nPlease enter the starting integer for the mood of this NPC, from -10 to 10"
                    "\nPositive integers means positive mood, "
                    "negative means a starting negative mood:"
                )
                npc_mood = util.prompt_number(False)
                if float(npc_mood) > 10 or float(npc_mood) < -10:
                    print("Input must be between -10 and 10. Trying again. . .")
                else:
                    npc['mood'] = npc_mood
                    break

        # Actions
        elif option == 6:
            # TODO: prompt if actions are wanting to be deleted
            print("\nNow adding dialogue actions to this NPC. . .")
            actions = add_actions()
            npc['actions'] = actions

        # Scenes
        elif option == 7:
            # TODO: same here
            print("\nNow adding dialogue trees to this NPC. . .")
            scenes = create_scene(npc['id'])
            npc['scenes'] = scenes

    def modify_scene(scene: dict):
        """
        Modifies an existing scene

        Args:
            scene (dict):
                The scene to modify
        Returns:
            None
        """
        print("Modifying scene. . .")
        # prompt what attribute to modify via list
        print("Please enter the number attribute you would like to modify:\n")
        print(
            "1. ID\n"
            "2. Name\n"
            "3. Dialogues\n"
        )
        while True:
            option = util.prompt_number(False)

        # access the scene data via ID given in NPC data


    def modify(args: list):
        """
        Modifies an instance of an NPC or scene

        Args:
            args: list
                the arguments passed to the command
        Returns:
            None
        """
        info = {
            "help": "create a new instance of NPC or scene.\n \
            Args:\n\
                type: The type of the instance you want to modify (NPC or Scene)\n\
                npc_id: The ID of NPC or scene to modify",
            "args": ['type', 'npc_id']
        }

        if not args:
            print("Arguments required for modify command. Type 'help' for more information.")
            return

        if args[0] == 'help':
            print(info['help'])
        else:
            print("NPC ID:\n")
            npc_id = util.prompt_id()
            if not npc_id:
                print("NPC ID needed for modify command")
                print("Trying again. . .")
                # Check if NPC exists
                # Grab NPC's data, sotre locally
            # NPC Modification
            if args[0].lower() == 'npc':
                # Open the NPC data's entry, edit directly
                pass
            # Scene Modification
            elif args[0].lower() == 'scene':
                # Enter Scene ID
                print("Scene ID:\n")
                npc_id = util.prompt_id()

                # Check if Scene exists

                # Grab NPC's scene data

            else:
                pass
