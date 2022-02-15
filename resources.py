
class Character:
    def __init__(self, name, health, attack, armor) -> None:
        self.name=name
        self.health=health
        self.attack=attack
        self.armor=armor
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nhealth {self.health}\nattack {self.attack}\narmor {self.armor}"
    
    def attack(self):
        return self.attack
    
    def take_damage(self, damage):
        relative_damage = damage-self.armor
        self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_health(self):
        return self.health

class Goblin:
    def __init__(self, health, attack, armor):
        self.health=health
        self.attack=attack
        self.armor=armor
    
    def __str__(self) -> str:
        return f"Goblin\nhealth {self.health}\nattack {self.attack}\narmor {self.armor}"

    def attack(self):
        return self.attack
    
    def take_damage(self, damage):
        relative_damage = damage-self.armor
        self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_health(self):
        return self.health


        