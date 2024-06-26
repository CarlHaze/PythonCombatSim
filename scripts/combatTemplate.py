import random
import time
import csv
from items import items
from nameGen import generate_random_name_from_csv

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

        # Check if defender is still alive
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
            return attacker, defender  # Return the winner and loser

        # Swap attacker and defender for next round
        attacker, defender = defender, attacker

def record_combat_history(winner_name, winner_item, winner_health, opponent_name, opponent_item):
    with open("G:/PythonCombatSim/data/combatHistory.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([winner_name, winner_item, winner_health, opponent_name, opponent_item])

def run_combat_multiple_times():
    try:
        num_times = int(input("How many times do you want to run the combat simulation? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for _ in range(num_times):
        player1_name = generate_random_name_from_csv("G:/PythonCombatSim/data/names.csv")
        player2_name = generate_random_name_from_csv("G:/PythonCombatSim/data/names.csv")
        player1 = Character(player1_name, 100, 10, 5, 5)  
        player2 = Character(player2_name, 100, 10, 5, 5)

        # Randomly select and equip items
        item_names = list(items.keys())
        random.shuffle(item_names)  # Shuffle the item names list

        player1_item = items[item_names[0]]
        player2_item = items[item_names[1]]

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
        winner, loser = combat(player1, player2)
        print(f"{winner.name} wins the combat against {loser.name}!")

       # Record the combat details to the combat history CSV file
        record_combat_history(winner.name, player1_item.name if winner == player1 else player2_item.name, winner.health,
                       loser.name, player1_item.name if loser == player1 else player2_item.name)


if __name__ == "__main__":
    run_combat_multiple_times()
