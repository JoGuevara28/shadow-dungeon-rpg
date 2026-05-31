Shadow Dungeon RPG

Created by Jorge Guevara Chavarría

Shadow Dungeon RPG is a hobby Python terminal game created to practice basic programming concepts such as object-oriented programming, functions, classes, user input, loops, conditionals, and file organization.

The game is a simple text-based RPG where the player explores a dungeon, fights enemies, uses potions, collects gold, and tries to survive.

Project Purpose

The main goal of this project is to review and practice Python fundamentals in a more complete project instead of only doing isolated exercises.

This project focuses on:

* Object-Oriented Programming
* Classes and objects
* Functions and methods
* User input with `input()`
* Conditional logic
* Loops
* Imports between Python files
* Basic terminal interaction
* Git and GitHub version control

Game Description

In Shadow Dungeon RPG, the player creates a character and enters a dungeon. The player can explore, view stats, use potions, and fight enemies.

During combat, the player can:

Attack the enemy
Use a potion
Run from battle

If the player defeats an enemy, they earn gold as a reward. If the player's health reaches zero, the adventure ends.

Project Structure


shadow-dungeon-rpg/
│
├── main.py
├── game.py
├── player.py
├── enemy.py
└── README.md


Files

### `main.py`

Starts the program and creates the main game object.

### `game.py`

Contains the main game flow, including:

* Main menu
* Adventure menu
* Exploration
* Combat system
* Potion usage
* Rewards
* Instructions

### `player.py`

Contains the `Player` class.

The player has:

* Name
* Health
* Attack power
* Defense
* Gold
* Potions

### `enemy.py`

Contains the `Enemy` class.

Each enemy has:

* Name
* Health
* Attack power
* Gold reward
* Experience reward

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/shadow-dungeon-rpg.git
```

2. Move into the project folder:

```bash
cd shadow-dungeon-rpg
```

3. Run the program:

```bash
python3 main.py
```

## Example Gameplay

```text
=============WELCOME TO THE SHADOW DUNGEON RPG=============
1. Start Game
2. How to Play
3. Exit

Select one option: 1
Starting a new adventure...
Enter your player's name: Jorge

=============Adventure Menu=============
1. Explore
2. View stats
3. Use potion
4. Return to main menu
```

## Features

* Terminal-based gameplay
* Player creation
* Main menu and adventure menu
* Combat system
* Enemy encounters
* Potion system
* Gold rewards
* Basic input validation
* Object-oriented structure

## Future Improvements

Some possible future improvements include:

* Add different enemy types
* Add random dungeon events
* Add weapons and armor
* Add a level-up system
* Add a final boss
* Add save/load functionality
* Improve the story and dungeon descriptions

## Technologies Used

* Python
* Git
* GitHub
* Command Line

## Author

Created by **Jorge Guevara Chavarría** as a hobby project to practice Python, object-oriented programming, functions, and terminal-based application development.
