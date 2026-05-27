class Player:

    def __init__(self, name, health = 100, max_health = 100, attack_power = 15, defense = 5, gold = 0, potions = 2):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.gold = gold
        self.potions = potions

    def show_stats(self):
        print(self.name)
        print(self.health)
        print(self.max_health)
        print(self.attack_power)
        print(self.defense)
        print(self.gold)
        print(self.potions)

    def take_damage(self, amount):
        real_damage = amount - self.defense
        if real_damage < 0:
            real_damage = 0
        self.health = self.health - real_damage
        if self.health <= 0:
            self.health = 0
        return real_damage

    def heal(self):
        if self.potions <= 0:
            return "You don't have potions"
        self.health += 30
        self.potions -= 1
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"You have {self.health}/{self.max_health} HP")
        return 'You used a potion'
        

    def is_alive(self):
        if self.health <= 0:
            return False
        return True
