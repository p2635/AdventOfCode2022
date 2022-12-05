from Rucksack import Rucksack
from RucksackAnalyser import get_item_priority

# Data handling
file = open("input/d3.txt", encoding="utf-8", mode="r")
rucksacks = file.readlines()
file.close()
 # Clean it so there are no new lines (\n) characters
rucksacks = [line.strip() for line in rucksacks]

# Part 1
totalPriority = 0

for line in rucksacks:
    rucksack = Rucksack(line)
    common_item = rucksack.get_common_item()
    totalPriority += get_item_priority(common_item)

print("The answer to part 1 should be", totalPriority)
