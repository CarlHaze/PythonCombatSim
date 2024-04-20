import random
import csv

def generate_random_name_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        names = list(reader)
    
    first_names = [row[0] for row in names]
    last_names = [row[1] for row in names]
    
    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    
    return f"{random_first_name} {random_last_name}"

if __name__ == "__main__":
    random_name = generate_random_name_from_csv("G:/PythonCombatSim/data/names.csv")
    print(random_name)
