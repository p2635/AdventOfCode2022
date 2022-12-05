from Cargo import Cargo
from string import ascii_uppercase as upper

# Just for testing
def hello():
    return "hello"

# First thing is to get the drawing of the stacks
# read line until you get to an empty line

with open("input/d5.txt", encoding='utf-8', mode="r") as file:

    # Store the original cargo map
    map = []
    for line in file:
        if "1" in line:
            break
        else:
            map.append(line)

    # Put this map into a cargo object
    cargo = Cargo(map)

    # Check that it still looks right
    for line in cargo.map:
        print(line)


    length = 0
    # Check the stack size
    for line in cargo.map:
        for char in line:
            if char in upper:
                print(char)
                length += 1
    
    print(f"The stack size is {length}")

# find out how many stacks there are
# populate the stacks