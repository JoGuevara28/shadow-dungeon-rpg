"""
Created by Jorge Guevara Chavarría
Game class for Shadow Dungeon RPG.
This file contains the main game flow:
- Main menu
- Adventure menu
- Player creation
- Exploration
- Combat system
- Potion usage
- Instructions
"""

from player import Player
from enemy import Enemy

class Game:

    def __init__(self):
        self.option = ""
        self.player = None

    def show_menu(self):
        """Displays the main menu."""
        print("=============WELCOME TO THE SHADOW DUNGEON RPG=============")
        print("1. Start Game")
        print("2. How to Play")
        print("3. Exit")

    def show_adventure_menu(self):
        """Displays the adventure menu after the player starts the game."""
        print("=============Adventure Menu=============")
        print("1. Explore")
        print("2. View stats")
        print("3. Use potion")
        print("4. Return to main menu")

    def start(self):
        """Starts the main menu loop."""
        while True:
            self.show_menu()
            self.option = input("Select one option: ")
            match self.option:
                case "1":
                    self.start_game()

                case "2":
                    self.how_to_play()

                case "3":
                    print("Leaving the program")
                    break

                case _:
                    print("Invalid option.")

    def start_game(self):
        """
        Starts a new adventure.
        This method asks for the player's name,
        creates a Player object, and opens the adventure menu.
        """
        print("Starting a new adventure...")
        player_name = input("Enter your player's name: ")
        if player_name.strip() == "":
            player_name = "Hero"
        self.player = Player(player_name)
        self.player.show_stats()
        self.adventure_menu()

    def adventure_menu(self):
        """Controls the adventure menu loop."""
        while self.player.is_alive():
            self.show_adventure_menu()
            self.option = input("Select one option: ")
            match self.option:
                case "1":
                    self.explore()

                case "2":
                    self.player.show_stats()

                case "3":
                    self.use_potion()

                case "4":
                    print("Returning to main menu...")
                    break

                case _:
                    print("Invalid option.")
        if not self.player.is_alive():
            print("Your adventure has ended.")

    def explore(self):
        """
        Allows the player to explore the dungeon.
        For now, exploring always creates a Monster enemy
        and starts a combat encounter.
        """
        print(f"{self.player.name} is exploring the dungeon...")
        enemy_player = Enemy("Monster")
        print(f"A {enemy_player.name} appeared!")
        print(f"{enemy_player.name} HP: {enemy_player.health}")
        self.combat(enemy_player)

    def combat(self, enemy_monster):
        """
        Handles combat between the player and an enemy.
        The player can attack, use a potion, or run.
        If the enemy survives the player's turn, it attacks back.
        """
        while self.player.is_alive() and enemy_monster.is_alive():

            print(f"Your HP: {self.player.health}/{self.player.max_health}")
            print(f"{enemy_monster.name} HP: {enemy_monster.health}")
            
            print("=============Choose your fight=============")
            print("1. Attack")
            print("2. Use potion")
            print("3. Run")
            self.option = input("Select one option: ")
            match self.option:
                case "1":
                    damage = enemy_monster.take_damage(self.player.attack_power)
                    print(f"You dealt {damage} damage to {enemy_monster.name}.")

                case "2":
                    print(self.player.heal())

                case "3":
                    print("You're running from the enemy...")
                    break

                case _:
                    print("Invalid option.")

            if enemy_monster.is_alive():
                damage = self.player.take_damage(enemy_monster.attack_power)
                print(f"{enemy_monster.name} attacked you and dealt {damage} damage.")

        if not self.player.is_alive():
            print("You lose.")

        if not enemy_monster.is_alive():
            print(f"You defeated {enemy_monster.name}. You win!")
            self.give_reward(enemy_monster)

    def give_reward(self, enemy_monster):
        """
        Gives gold to the player after defeating an enemy.
        """
        self.player.gold += enemy_monster.gold_reward
        print(f"You earned {enemy_monster.gold_reward} gold.")
        print(f"Total gold: {self.player.gold}")

    def use_potion(self):
        """Allows the player to use a potion from the adventure menu."""
        print(self.player.heal())

    def how_to_play(self):
        """Displays basic instructions for the game."""
        print("Explore rooms, fight enemies, collect gold, use potions, and defeat the final boss.")
