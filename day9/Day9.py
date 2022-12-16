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

# Updates grid with specific trail of a rope
def update_grid_with_rope_trail(rope):
    grid[rope[0]][rope[1]] = 1
    return rope

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

def rope_follows_accordingly(rope1, rope2):
    
    y_diff = rope1[0] - rope2[0]
    x_diff = rope1[1] - rope2[1]

    # If rope1 is 2 steps UDLR, move rope2 1 UDLR.
    if y_diff == 0:
        if x_diff == 2:
            move(rope2, "R")
        elif x_diff == -2:
            move(rope2, "L")
    elif x_diff == 0:
        if y_diff == 2:
            move(rope2, "D")
        elif y_diff == -2:
            move(rope2, "U")

    # Diagonals
    if y_diff == 2 and x_diff in (1, 2) \
        or y_diff == 1 and x_diff == 2:
        move(rope2, "R")
        move(rope2, "D")
    elif y_diff == 2 and x_diff in (-1, -2) \
        or y_diff == 1 and x_diff == -2:
        move(rope2, "L")
        move(rope2, "D")
    elif y_diff == -2 and x_diff in (-1, -2) \
        or y_diff == -1 and x_diff == -2:
        move(rope2, "L")
        move(rope2, "U")
    elif y_diff == -2 and x_diff in (1, 2) \
        or y_diff == -1 and x_diff == 2:
        move(rope2, "R")
        move(rope2, "U")

##############################################################################
##
##           PART 1 - Head and tail rope
##
##############################################################################

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

# Head and tail start in the centre (notice the format is y, x)
head = [400, 400]
tail = [400, 400]
update_grid_with_rope_trail(tail) # Mark tail starting point

# Now let's go through the commands
for command in commands:

    direction = command[0]
    distance = command[1]

    # Update where head should be, step by step
    for steps in range(distance):
        move(head, direction)
        rope_follows_accordingly(head, tail)
        update_grid_with_rope_trail(tail)

# Let's add up all the pieces
where_tail_has_been = [number for row in grid for number in row if number != 0]
print(sum(where_tail_has_been))

##############################################################################
##
##           PART 2 - 10 knots
##
##############################################################################

# Reset the playing field
# Again, no idea how big the grid should be, let's just make it big.
grid = initiatize_grid(800, 800)

# Now we need ten knots, so 0 will be head and 9 will be tail
knots = [[400, 400] for knot in range(10)]
head = knots[0]
tail = knots[9]
update_grid_with_rope_trail(tail) # Mark tail starting point

# Now let's go through the commands
for command in commands:

    direction = command[0]
    distance = command[1]

    # Update where head should be, step by step
    for steps in range(distance):
        move(head, direction)
        
        # Other knots follow
        knot_tracker = 0
        while knot_tracker < len(knots) - 1:
            leading_rope = knots[knot_tracker]
            follower = knots[knot_tracker + 1]
            rope_follows_accordingly(leading_rope, follower)
            update_grid_with_rope_trail(tail)
            knot_tracker += 1

# Let's add up all the pieces
where_tail_has_been = [number for row in grid for number in row if number != 0]
print(sum(where_tail_has_been))
