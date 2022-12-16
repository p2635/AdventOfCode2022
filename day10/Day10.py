# Variables
x = 1
x_log = {1: x}

# Get the commands
with open("input/d10.txt", encoding='utf-8', mode="r") as file:
    commands = file.readlines()
commands = [command.split() for command in commands]

# Loop through and build an accurate list of commands
# that executes in alignment with cycles.
# In this version, addx actually adds to x on that cycle.

cycle_set = 0
accurate_commands = [] # The new list
while cycle_set < len(commands):

    current_command = commands[cycle_set]
    prev_command = commands[cycle_set-1]

    if 'noop' in current_command:
        accurate_commands.append(current_command)
    elif 'addx' in current_command:
        accurate_commands.append(['noop'])
        accurate_commands.append(current_command)
    else:
        print("Error, exiting program.")
        break

    cycle_set += 1

##############################################################################
##
##           PART 1 - Calculating signal strength
##
##############################################################################


# Now let's execute the program

cycle_set = 0
while cycle_set < len(accurate_commands):

    current_command = accurate_commands[cycle_set]

    if 'noop' in current_command:
        # Do nothing, just write down x.
        x_log.update({cycle_set + 2: x})
    elif 'addx' in current_command:
        # Add to x and write it down.
        x += int(current_command[1])
        x_log.update({cycle_set + 2: x})
    else:
        print("Error, exiting program.")
        break

    cycle_set += 1

# Log of x in each cycle
print(x_log)

# Signal strength (the cycle number multiplied by the value of the X register) 
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
signal_strength_cycles = {20, 60, 100, 140, 180, 220}
signal_strengths = [cycle * x_log[cycle] for cycle in x_log if cycle in signal_strength_cycles]        
print(f"The signal strengths for part 1 are {signal_strengths}.")
print(f"The sum of all these comes to {sum(signal_strengths)}.")

##############################################################################
##
##           PART 2 - The sprite
##
##############################################################################

# To get the pixel band so I know where to draw for the CRT
def get_sprite_position(sprite_pos = 0, sprite_width = 3):
    if sprite_pos < 0:
        sprite_pos = 0
    pixel_band = ['.' for pixel in range(40)]
    for position in range(sprite_pos, sprite_pos + sprite_width):
        try:
            pixel_band[position] = '#'
        except: # Having problems with index out of range
            pass
    return pixel_band

# To test the above function
def print_sprite_position():
    print(''.join((get_sprite_position())))

cycle_set = 0 # Controls when to start printing on a new line
pixel_width = 40 # Controls how wide each line is
while cycle_set < len(x_log):
    cycle_number = cycle_set + 1
    current_pixel_pos = 0
    while cycle_number < cycle_set + pixel_width:
        current_x_value = x_log[cycle_number] # Must be 1-240
        pixel_band = get_sprite_position(current_x_value - 1) # Must be x's value, -1 wraps around?
        print(f"{pixel_band[current_pixel_pos]}",end='') # Must be 0-39, what is j?? just a block of cycles.
        cycle_number += 1
        current_pixel_pos += 1
    print()
    cycle_set += pixel_width

# This program results in a key index error of 242, but I can fix that later. I think I got the solution!
# Heard to read the first letter, is it a P? PZHFGJCB? (wrong) It must be R or D? It was R (ugly looking one)
###..####.#..#.####..##....##..##..###.
##.#....#.#..#.#....#..#....#.#..#.#..#
##.#...#..####.###..#.......#.#....###.
###...#...#..#.#....#.##....#.#....#..#
###..#....#..#.#....#..#.#..#.#..#.#..#
####.####.#..#.#.....###..##...##..###.
