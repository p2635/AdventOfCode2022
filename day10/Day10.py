# Variables
x = 1
addx_cycle = 2
noop_cycle = 1

# Get the commands
with open("input/d10.txt", encoding='utf-8', mode="r") as file:
    commands = file.readlines()
commands = [command.split() for command in commands]

# Loop through and create a more accurate list of commands
# that would theoretically execute in alignment with cycles.
# In this version, addx actually adds to x on that cycle.

i = 0
accurate_commands = [] # The new list
while i < len(commands):

    current_command = commands[i]
    prev_command = commands[i-1]

    if 'noop' in current_command:
        if 'noop' in prev_command or i == 0: # Cheating a bit, I know noop is the first command
            accurate_commands.append(prev_command)
        elif 'addx' in prev_command:
            accurate_commands.append(prev_command)
    elif 'addx' in current_command:
        if 'noop' in prev_command:
            accurate_commands.append(prev_command)
        elif 'addx' in prev_command:
            accurate_commands.append(prev_command)
    else:
        print("Error, exiting program.")
        break

    i += 1

print(accurate_commands)
print(len(accurate_commands))
print(accurate_commands == commands)