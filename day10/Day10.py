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

i = 0
accurate_commands = [] # The new list
while i < len(commands):

    current_command = commands[i]
    prev_command = commands[i-1]

    if 'noop' in current_command:
        accurate_commands.append(current_command)
    elif 'addx' in current_command:
        accurate_commands.append(['noop'])
        accurate_commands.append(current_command)
    else:
        print("Error, exiting program.")
        break

    i += 1

# Now let's execute the program

i = 0
while i < len(accurate_commands):

    current_command = accurate_commands[i]

    if 'noop' in current_command:
        # Do nothing, just write down x.
        x_log.update({i + 2: x})
    elif 'addx' in current_command:
        # Add to x and write it down.
        x += int(current_command[1])
        x_log.update({i + 2: x})
    else:
        print("Error, exiting program.")
        break

    i += 1

# Log of x in each cycle
print(x_log)

# Signal strength (the cycle number multiplied by the value of the X register) 
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
signal_strength_cycles = {20, 60, 100, 140, 180, 220}
signal_strengths = [cycle * x_log[cycle] for cycle in x_log if cycle in signal_strength_cycles]        
print(f"The signal strengths for part 1 are {signal_strengths}.")
print(f"The sum of all these comes to {sum(signal_strengths)}.")
