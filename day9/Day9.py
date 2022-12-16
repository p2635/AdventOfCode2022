# Functions
def show_grid():
    print("=== SHOWING GRID ===")
    for row in grid:
        print(*row)

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

def update_grid():
    grid[head[0]][head[1]] = "H"

def move(knot, direction, steps):
    if direction == "U":
        knot[0] -= steps
    elif direction == "D":
        knot[0] += steps
    elif direction == "L":
        knot[1] -= steps
    elif direction == "R":
        knot[1] += steps

def update_tail():
    pass

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

# Now let's go through the commands (finally)
for command in commands:

    print(f"=== {command} ===")
    
    # Update where head should be
    move(head, command[0], (command[1]))
    print(head)

    # Reset grid before updating it
    grid = initiatize_grid(800, 800)
    update_grid()
    # show_grid()
