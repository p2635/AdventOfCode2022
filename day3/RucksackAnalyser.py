from string import ascii_uppercase as upper
from string import ascii_lowercase as lower

# Create the priority dictionary for lookups
alphabet = []
for i in lower:
    alphabet.append(i)
for i in upper:
    alphabet.append(i)

priority_table = {}

for i in range(len(alphabet)):
    priority_table.update({alphabet[i]: i+1})

# Get item priority based on priority table
def get_item_priority(char):
    return priority_table[char]

# Get item type, is it big or small?
def get_item_type(item):
    if item.isupper() == True:
        return 0 # If it's an uppercase, it's item type 0
    elif item.islower() == True:
        return 1 # If it's a lowercase, it's item type 1
    else:
        return "Something went wrong."

# Find the item type that appears in both compartments of each rucksack
def find_common_item(c1, c2):
    pass