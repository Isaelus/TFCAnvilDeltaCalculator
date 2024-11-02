from typing import List, Tuple
from itertools import combinations
import tkinter as tk
from tkinter import *

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

#info[0] is the target delta
#info[1] is the Combo Limit
#info[2] is the path to achieve target delta
info = [0, 6, ""]

#Updates Combo Limit
def updateMaxCombo(limit : int) -> None:
    info[1] = limit - 1
    deltaComboLimit.config(text=f"Max Combo Limit: {info[1]}")
    anvilCombo = findCombinations(-1 * info[0], info[1])
    if anvilCombo:
        temp = []
        for name, value in anvilCombo:
            temp.append(f"{name} ({value})")
        info[2] = ' -> '.join(temp)
    else:
        info[2] = "Not possible within constraints"
    
    deltaCombo.config(text=f"Combo: {info[2]}")
    
def addToDelta(amount : int) -> None:
    info[0] += amount
    delta.config(text=f"Delta: {-1 * info[0]}")
    anvilCombo = findCombinations(-1 * info[0], info[1])
    
    if anvilCombo:
        temp = []
        for name, value in anvilCombo:
            temp.append(f"{name} ({value})")
        info[2] = ' -> '.join(temp)
    else:
        info[2] = "Not possible within constraints"
    
    deltaCombo.config(text=f"Combo: {info[2]}")

def resetDelta() -> None:
    info[0] = 0
    info[2] = ""
    delta.config(text=f"Delta: {info[0]}")
    deltaCombo.config(text=f"Combo: {info[2]}")

#! This could probably be done with backtracking!
#Finds the least amount of hits required to achieve target delta
def findCombinations(target : List[int], maxHits : int) -> Tuple[Tuple[str, int]]:
    for r in range(1, maxHits):
        for combo in combinations(operations.items(), r):
            comboSum = 0
            for item in combo:
                comboSum += item[1]
                if comboSum == target:
                    return combo
    return []

root = tk.Tk()
root.geometry("600x400")
root.title("TFC Anvil Delta Calculator")

menuBar = tk.Menu(root)
root.config(menu=menuBar)

maxComboBar = tk.Menu(menuBar, tearoff=0, activebackground="lightblue", activeforeground="black")
menuBar.add_cascade(label='Max Combo', menu=maxComboBar)
maxComboBar.add_command(label='2', command=lambda: updateMaxCombo(3))
maxComboBar.add_command(label='3', command=lambda: updateMaxCombo(4))
maxComboBar.add_command(label='4', command=lambda: updateMaxCombo(5))
maxComboBar.add_command(label='5', command=lambda: updateMaxCombo(6))
maxComboBar.add_command(label='6', command=lambda: updateMaxCombo(7))

punchButton = tk.Button(root, text="Punch", command=lambda: addToDelta(2))
bendButton = tk.Button(root, text="Bend", command=lambda: addToDelta(7))
upsetButton = tk.Button(root, text="Upset", command=lambda: addToDelta(13))
shrinkButton = tk.Button(root, text="Shrink", command=lambda: addToDelta(16))
lHitButton = tk.Button(root, text="Light Hit", command=lambda: addToDelta(-3))
mHitButton = tk.Button(root, text="Medium Hit", command=lambda: addToDelta(-6))
hHitButton = tk.Button(root, text="Heavy Hit", command=lambda: addToDelta(-9))
drawButton = tk.Button(root, text="Draw", command=lambda: addToDelta(-15))
resetButton = tk.Button(root, text="Reset Delta", command=resetDelta)

punchButton.pack(pady=3)
bendButton.pack(pady=3)
upsetButton.pack(pady=3)
shrinkButton.pack(pady=3)
lHitButton.pack(pady=3)
mHitButton.pack(pady=3)
hHitButton.pack(pady=3)
drawButton.pack(pady=3)
resetButton.pack(pady=3)

delta = tk.Label(root, text=f"Delta: {info[0]}")
deltaCombo = tk.Label(root, text=f"Combo: {info[2]}")
deltaComboLimit = tk.Label(root, text=f"Max Combo Limit: {info[1]}")
delta.pack(pady=5)
deltaCombo.pack(pady= 5)
deltaComboLimit.pack(pady=5)

root.mainloop()

