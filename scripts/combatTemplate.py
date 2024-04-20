import random
import time
from items import items

class Character:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

def combat(player1, player2):
    # Determine who attacks first based on speed
    if player1.speed > player2.speed:
        attacker = player1
        defender = player2
    elif player2.speed > player1.speed:
        attacker = player2
        defender = player1
    else:  # If both have the same speed, randomly select attacker
        attacker = random.choice([player1, player2])
        defender = player1 if attacker == player2 else player2

    while player1.is_alive() and player2.is_alive():
        # Attacker attacks defender
        damage = random.randint(1, 5)
        defender.take_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {damage} damage.")
        time.sleep(0.5)

        # Check if defender is still alive
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
            break

        # Swap attacker and defender for next round
        attacker, defender = defender, attacker


if __name__ == "__main__":
    # Create characters
    player1 = Character("Player 1", 100, 10, 5, 5)  # Add speed attribute
    player2 = Character("Player 2", 100, 10, 5, 5)  # Add speed attribute

    # Randomly select and equip items
    item_names = list(items.keys())
    item_name_player1 = random.choice(item_names)
    item_name_player2 = random.choice(item_names)
    
    player1_item = items[item_name_player1]
    player2_item = items[item_name_player2]
    
    player1.attack += player1_item.attack_bonus
    player1.defense += player1_item.defense_bonus
    player1.speed += player1_item.speed_bonus
    
    player2.attack += player2_item.attack_bonus
    player2.defense += player2_item.defense_bonus
    player2.speed += player2_item.speed_bonus

    # Announce equipped items and bonuses
    print(f"{player1.name} equipped {player1_item.name} (Attack +{player1_item.attack_bonus}, Defense +{player1_item.defense_bonus}, Speed +{player1_item.speed_bonus})")
    print(f"{player2.name} equipped {player2_item.name} (Attack +{player2_item.attack_bonus}, Defense +{player2_item.defense_bonus}, Speed +{player2_item.speed_bonus})")

    # Start combat
    combat(player1, player2)
