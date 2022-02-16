
class Character:

    def __init__(self, name, health, attack, armor) -> None:
        self.name=name
        self.health=health
        self.attack=attack
        self.armor=armor
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nhealth {self.health}\nattack {self.attack}\narmor {self.armor}"
    
   
    
    def take_damage(self, damage):
        relative_damage = damage-self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_attack(self):
        return self.attack
        
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name


class Goblin:
    
    def __init__(self, health, attack, armor, id):
        self.health=health
        self.attack=attack
        self.armor=armor
        self.id=id
    
    def __str__(self) -> str:
        return f"Goblin\nhealth {self.health}\nattack {self.attack}\narmor {self.armor}\n {self.id}"

   
    
    def take_damage(self, damage):
        relative_damage = damage-self.armor
        if relative_damage < 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
     
    def get_name(self):
        return f"Goblin {self.id}"


        