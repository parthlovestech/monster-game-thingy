import random

class Character():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
        
    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        return damage
    
    def is_alive(self):
        return self.health > 0
    


class Game():
    def __init__(self):
        self.player = Character("Hero", 100, 20)
        self.monster = Character("Monster", 80, 15)
        
    
    def battle(self):
        print("The battle begins!")
        
        while self.player.is_alive() and self.monster.is_alive():
            print(f"\nYour health: {self.player.health}")
            print(f"\nMonster's health: {self.monster.health}")
            print("-"*20)
            
            
            action = input("Choose your action: (1) Attack, (2) Do nothing cause you have a skill issue: ")
            
            if action == "1":
                self.player.attack(self.monster)
            elif action =="2":
                print("You suck.")
            else:
                print("Invalid choice, you have a skill issue.")
                
            if not self.monster.is_alive():
                print(f"\n The {self.monster.name} has been defeated!")
                break
            
            print("\nThe monster attacks!")
            self.monster.attack(self.player)
            
            if not self.player.is_alive():
                print(f"\nYou have been defeated by {self.monster.name}!")
                break
            print ("Game Over!")
        

if __name__ == "__main__":
    game = Game()
    game.battle()
