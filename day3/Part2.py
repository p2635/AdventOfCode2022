import collections
from Rucksack import *
from RucksackAnalyser import *

# Data handling
file = open("input/d3.txt", encoding="utf-8", mode="r")
rucksacks = file.readlines()
file.close()

# Clean it so there are no new lines (\n) characters
rucksacks = [line.strip() for line in rucksacks]

# Go to each elf and tell them to throw out duplicate items
# This is prep for the next step to more easily search the badge
uniquesacks = []

for rucksack in rucksacks:
    uniquesack = ""
    for item in rucksack:
        if uniquesack.find(item) == -1:
            uniquesack += item
        else:
            pass
    uniquesacks.append(uniquesack)

# Part 2
totalPriority = 0

# Split the unique rucksacks list into chunks of 3
chunk_size = 3
elf_groups = list(split(uniquesacks, 3))

# Evaluate each elf group to find the common item
for group in elf_groups:
    
    # Bring out a clipboard to do a tally of unique items
    tally = collections.defaultdict(int)
    
    # Search the bags and make a tally
    for bag in group:
        for item in bag:
            tally[item] += 1

    # Variable for badge priority
    badge_priority = 0

    # Find the badge (common item) and its priority
    for item, count in tally.items():
        if count == 3:
            badge_priority = get_item_priority(item)

    # Add to the total priority then move on to the next group
    totalPriority += badge_priority

print("The answer to part 2 should be", totalPriority)
