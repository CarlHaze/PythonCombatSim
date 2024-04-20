import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_winning_items(csv_file):
    # Read the CSV file into a DataFrame, skipping the first row for data
    df = pd.read_csv(csv_file, skiprows=1)

    # Count occurrences of each value in the second column
    item_counts = df.iloc[:, 1].value_counts()

    # Plot the results
    item_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Count of winner items')
    plt.xlabel('Item')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Save the plot to a file in the data folder
    plt.savefig(f"G:/PythonCombatSim/data/CombatResults_{current_date}.png")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    csv_file = "G:/PythonCombatSim/data/combatHistory.csv"
    plot_winning_items(csv_file)
