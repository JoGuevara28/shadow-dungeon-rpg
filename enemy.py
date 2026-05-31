"""
Created by Jorge Guevara Chavarría

Enemy class for Shadow Dungeon RPG.

This class represents enemies in the game.
Each enemy has health, attack power, gold reward,
and experience reward.
"""
class Enemy:
    def __init__(
        self,
        name="Monster",
        health=100,
        attack_power=15,
        gold_reward=50,
        experience_reward=20
    ):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.gold_reward = gold_reward
        self.experience_reward = experience_reward

    def take_damage(self, amount):
        """
        Reduces the enemy's health based on incoming damage.
        Health cannot go below 0.
        """
        real_damage = amount
        if real_damage < 0:
            real_damage = 0
        self.health -= real_damage
        if self.health < 0:
            self.health = 0
        return real_damage
    
    def is_alive(self):
        """Returns True if the enemy is still alive."""
        if self.health <= 0:
            return False
        return True
