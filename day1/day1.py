# Advent of Code 2022 - Day 1
# https://adventofcode.com/2022/day/1
# Author: Philip Wong

# Get an inventory of foods that Python understands
inventory = []

# Let's open the file
with open("day1/puzzle_input.txt", encoding="utf-8", mode="r") as foods:
    
    # Elves line up, let's take down your details!
    currentElf = []

    for food in foods:

        # If you got food to show, let's build a list for you Elf!
        if food != "\n":
            currentElf.append(int(food))

        # No food? Put this in the inventory, move on to the next Elf.
        else:
            inventory.append(currentElf)
            currentElf = []

# How many elves are there?
print("Day 1 - Advent of Code")
print("Here are the latest stats...")
POPULATION = len(inventory)
print(f"* There are {POPULATION} elves.")

# Creating the total calories list
totalcals = []
for elf in inventory:
    totalcals.append(sum(elf))

# Finding the one who owns the most calorie-dense foods
mostCals = max(totalcals)
winningElf = totalcals.index(mostCals)
print(f"The winner of the competition holds {mostCals} calories, held by elf number {winningElf}!!!")