
class Character:
    def __init__(self, name, health, attack, armor) -> None:
        self.name=name
        self.health=health
        self.attack=attack
        self.armor=armor
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nhealth {self.health}\n attack {self.attack}\n armor {self.armor}"

class Goblin:
    def __init__(self, health, attack, armor) -> None:
        self.health=health
        self.attack=attack
        self.armor=armor
    
    def __str__(self) -> str:
        return f"Goblin\nhealth {self.health}\narmor {self.armor}"
        