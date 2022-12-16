# Functions
def initiatize_grid(rows, columns):
    return [[0] * columns for i in range(rows)]
    # Looks similar to this:
    # 0 [0, 0, 0, 0, 0, 0],
    # 1 [0, 0, 0, 0, 0, 0],
    # 2 [0, 0, 0, 0, 0, 0],
    # 3 [0, 0, 0, 0, 0, 0],
    # 4 [0, 0, 0, 0, 0, 0],
    # 5 [0, 0, 0, 0, 0, 0]
    #    0  1  2  3  4  5

# Updates where the tail has been, not head
def update_grid_head():
    grid[head[0]][head[1]] = 1
    return head

# Updates where the tail has been, not head
def update_grid_tail():
    grid[tail[0]][tail[1]] = 1
    return tail

# This does the move immediately, but the challenge requires step by step
def move(knot, direction, steps = 1):
    if direction == "U":
        knot[0] -= steps
    elif direction == "D":
        knot[0] += steps
    elif direction == "L":
        knot[1] -= steps
    elif direction == "R":
        knot[1] += steps
    else:
        return "Error"
    return f"Moved {knot} {direction} by {steps}."

# SOMETHING WRONG - FIX THIS
def tail_follows_accordingly():
    
    y_diff = head[0] - tail[0]
    x_diff = head[1] - tail[1]

    # If head is 2 steps UDLR, move tail 1 UDLR.
    if y_diff == 0:
        if x_diff == 2:
            move(tail, "R")
        elif x_diff == -2:
            move(tail, "L")
    elif x_diff == 0:
        if y_diff == 2:
            move(tail, "D")
        elif y_diff == -2:
            move(tail, "U")

    # Diagonals
    if y_diff == 2 and x_diff == 1 \
        or y_diff == 1 and x_diff == 2:
        move(tail, "R")
        move(tail, "D")
    elif y_diff == 2 and x_diff == -1 \
        or y_diff == 1 and x_diff == -2:
        move(tail, "L")
        move(tail, "D")
    elif y_diff == -2 and x_diff == -1 \
        or y_diff == -1 and x_diff == -2:
        move(tail, "L")
        move(tail, "U")
    elif y_diff == -2 and x_diff == 1 \
        or y_diff == -1 and x_diff == 2:
        move(tail, "R")
        move(tail, "U")

# The Main Stuff

# Process the input text file
with open("input/d9.txt", encoding="utf-8", mode="r") as file:
    # Command 0 = Direction, Command 1 = Steps
    commands = [command.strip().split() for command in file]

# Convert the second part of the command to be an int
i = 0
while i < len(commands):
    commands[i][1] = int(commands[i][1])
    i += 1

# I have no idea how big the grid should be, let's just make it big.
grid = initiatize_grid(800, 800)

# Head and tail start at the bottom left (notice the format is y, x)
head = [400, 400]
tail = [400, 400]
update_grid_tail() # Mark tail starting point

# Now let's go through the commands (finally)
for command in commands:

    direction = command[0]
    distance = command[1]

    # Update where head should be, step by step
    for steps in range(distance):
        move(head, direction)
        tail_follows_accordingly()
        update_grid_tail()

# Let's add up all the pieces
where_tail_has_been = [number for row in grid for number in row if number != 0]
print(sum(where_tail_has_been))
