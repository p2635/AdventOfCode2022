# Text File Parser

import re

# Variables that might be useful

HEIGHT = 8   # Stores the cargo height (no. of items)
COUNT = 9    # Stores the cargo count (width)
LENGTH = 3      # Stores the cargo char length
GAP = 1      # Stores cargo gap char length

# Determines how many cargo based on one line of text
def check_cargo_countrow(row):
    cargo_count = (len(row) + GAP) / LENGTH
    return int(cargo_count)

# Turns a line of text into a Python list
def line_to_list(line):
    step = LENGTH + GAP
    return [line[i] for i in range(1, len(line), step)]

# Turns a drawing into a Python list of lists
# to prepare for processing
def translate_map(drawing):

    # Build the map
    main_list = []
    for line in drawing:
        main_list.append(line_to_list(line))

    # Transpose the map so it's the right way around
    main_list = list(map(list,zip(*main_list)))
    
    # Remove all the blanks
    # Reverse it as well afterwards (again so it's the right way)
    new_list = []
    for i in main_list:
        clean = [x for x in i if x != " "]
        clean = list(reversed(clean))
        new_list.append(clean)

    return new_list

# Parse a line of instructions
def parse_line_of_instruction(str):
    numbers = re.findall(r'\d+', str)
    # Convert to an int list instead
    numbers = [int(x) for x in numbers]
    return numbers
