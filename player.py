"""
Created by Jorge Guevara Chavarría

Player class for Shadow Dungeon RPG.

This class represents the player.
It stores player attributes such as health, attack power,
defense, gold, and potions. It also contains methods for
taking damage, healing, checking if the player is alive,
and displaying player statistics.
"""

class Player:

    def __init__(
        self,
        name,
        health=100,
        max_health=100,
        attack_power=15,
        defense=5,
        gold=0,
        potions=2
    ):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.gold = gold
        self.potions = potions

    def show_stats(self):
        """Displays the player's current statistics."""
        print("=============Player Stats=============")
        print(f"Name: {self.name}")
        print(f"HP: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack_power}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")
        print(f"Potions: {self.potions}")

    def take_damage(self, amount):
        """
        Reduces the player's health based on incoming damage.

        The player's defense reduces the final damage taken.
        Health cannot go below 0.
        """
        real_damage = amount - self.defense
        if real_damage < 0:
            real_damage = 0
        self.health -= real_damage
        if self.health < 0:
            self.health = 0
        return real_damage

    def heal(self):
        """
        Uses one potion to heal the player.
        The player heals 30 HP per potion.
        Health cannot go above max_health.
        """
        if self.potions <= 0:
            return "You don't have potions"
        self.health += 30
        self.potions -= 1
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"You have {self.health}/{self.max_health} HP")
        return "You used a potion"

    def is_alive(self):
        """Returns True if the player is still alive."""
        if self.health <= 0:
            return False
        return True
