# Dialogue Tree

This module is used to store units for Scenes and Dialogues, that comprise a Dialogue Tree.

The developer can implement their own traversal algorithm within the context of their project. This module will allow for creation of trees, manipulation of trees, and basic traversal of trees

---

## Tree Overview

A Dialogue Tree is a tree of dialogue options that the user can choose from
This module allows for manipulation of the tree, such as adding or removing nodes
Traversal of the tree is also possible, allowing for the user to choose a path through the tree.

### SCENE Objects

#### Scene ID

- This is how we know what to show the user and decide what the starting dialogue should be

#### Starting Dialogue ID

- This will lead to the first Dialogue which then leads to an Action onject

### DIALOGUE Objects

#### Dialogue ID

- This is what corresponds with an NPC object

#### Text

- This is the actual words associated with the piece of dialogue

#### Options for responses (OPTIONAL)

- These are pieces of text that the USER chooses in response to the Dialogue
- These are known as "REPLIES"

### ACTION Objects

#### Action ID

- This is what corresponds with a response or a piece of dialogue

#### Previous Dialogue ID

- Leads back to the dialogue choice that came with this Reply object

#### NEXT ID

- Leads to the NEXT Dialogue object

#### Special Attributes (Optional Metadata)

- Dictionary of unique features associated with the action object, defined by the developer

---

These objects, specifically the Dialogue and Reply objects, are used to create a link between each other.
We can then chain these links together to create a "tree" of dialogue options.

Each object also has a context that can be used to store information about the object, that is defined by the developer.
This can contain any relevant information that may change the flow of dialogue,
such as the player's inventory or the current location, or relationship with NPCs.

## Example Usage

```python
    root = Scene(1, 1)
    tree = Tree(root)
    next_scene = tree.traverse(2)
```
