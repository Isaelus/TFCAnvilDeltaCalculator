from itertools import combinations
import tkinter
from tkinter import *
import sv_ttk
#
#root = tkinter.Tk()
#root.title("TFC Hammer Delta Calculator")

#Label(root, text="Delta Required").grid(row=0)

#sv_ttk.set_theme("dark")

#root.mainloop()

operations = {
    "Punch": 2,
    "Bend": 7,
    "Upset": 13,
    "Shrink": 16,
    "Light Hit": -3,
    "Medium Hit": -6,
    "Heavy Hit": -9,
    "Draw": -15
}

# Set the target deltas
target_deltas = [-20, -17, -14, -16]

# Function to find combinations that match a target delta
def find_combinations(target):
    results = []
    # Check combinations from 2 to 4 operations
    for r in range(2, 5):
        for combo in combinations(operations.items(), r):
            # Calculate the sum of the chosen combination
            combo_sum = sum(item[1] for item in combo)
            if combo_sum == target:
                results.append(combo)
    return results

# Run the function for each target delta
for delta in target_deltas:
    print(f"Combinations for target delta {delta}:")
    combinations_found = find_combinations(delta)
    if combinations_found:
        for combo in combinations_found:
            combo_str = " + ".join(f"{name} ({value})" for name, value in combo)
            print(f"  {combo_str} = {delta}")
    else:
        print("  No combinations found.")
    print()