from string import ascii_uppercase as upper
from string import ascii_lowercase as lower

# Create the priority dictionary for lookups
alphabet = [i for i in (lower + upper)]
priority_table = {}
for i in range(len(alphabet)):
    priority_table.update({alphabet[i]: i+1})

# Get item priority based on priority table
def get_item_priority(char):
    return priority_table[char]

# Split a list by even chunks
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
