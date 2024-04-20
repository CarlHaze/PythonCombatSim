class Item:
    def __init__(self, name, attack_bonus=0, defense_bonus=0, speed_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.speed_bonus = speed_bonus

items = {
    "Sword": Item("Sword", attack_bonus=5),
    "Shield": Item("Shield", defense_bonus=5),
    "Leather Boots" : Item("Boots", speed_bonus=5)
    # Add more items here
}
