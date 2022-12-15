import math

##############################################################################
##
##           Day 8 - Treetop Tree House
##
##############################################################################

# Create 2D array
with open("input/d8.txt", mode = "r") as file:
    lines = file.readlines()

# Remove the newline character from each line
lines = [line.strip() for line in lines]

# Convert to an int list of lists
trees = [[int(char) for char in line] for line in lines]

# Output data about the text file
trees_x = len(trees)
trees_y = len(trees[0])
print(f"There are {trees_x} rows and {trees_y} columns.")

##############################################################################
##
##           PART 1 - This challenge is about counting visible trees.
##
##############################################################################

visible_trees = 0

# If it's the first or last row/column, then those trees are visible by default
edge_trees = 2*(trees_x + trees_y) - 4
visible_trees += edge_trees
print(f"Around the edge, there are {visible_trees} visible trees.")

# Give a list of trees, determine if each tree is visible

# Indexes to start counting from (start inspecting only the inside, not the edge)
start = 1
end_row = trees_x - 1
end_column = trees_y - 1

# Keep track of the row
this_row = start
while this_row < end_row:

    # Keep track of the tree
    this_tree = start

    # Begin the checking
    # A tree is visible if it is tallest in ANY ONE direction (up, down, left, right)
    while this_tree < end_column:

        # Keep track of the tree height
        this_tree_height = trees[this_row][this_tree]

        # Get the column of trees aligned with tree to inspect
        column = [row_of_trees[this_tree] for row_of_trees in trees]

        # Look up, down, left, right, which tree is the tallest?
        up = max(column[:this_row])
        down = max(column[this_row + 1:trees_y])
        left = max(trees[this_row][:this_tree])
        right = max(trees[this_row][this_tree + 1:trees_y])
        tallest_trees_around_me = [up, down, left, right]

        # Compare tree height
        for tallest in tallest_trees_around_me:
            if this_tree_height > tallest:
                # If this is true, increment visible trees count
                visible_trees += 1
                break

        # Move on to the next tree
        this_tree += 1

    # Move on to the next row of trees
    this_row += 1

print(f"Total number of visible trees is {visible_trees}.")

##############################################################################
##
##           PART 2 - This challenge is about calculating scenic score.
##
##############################################################################

highest_scenic_score = 0

# Calculate scenic score
see_x_trees = 0

def I_see_x_trees(trees, my_tree_height):

    x = 0

    # In case it's an edge tree
    if trees is []:
        return 1

    # Otherwise look ahead to the distance
    for tree in trees:
        if this_tree_height > tree:
            x += 1
        else:
            x += 1
            break
    return x

# Keep track of the row
this_row = 0
while this_row < trees_x:

    # Keep track of the tree
    this_tree = 0

    # Begin the checking
    while this_tree < trees_y:

        # Keep track of the tree height
        this_tree_height = trees[this_row][this_tree]

        # Get the column of trees aligned with tree to inspect
        column = [row_of_trees[this_tree] for row_of_trees in trees]

        # Look up, down, left, right
        up = column[:this_row]
        down = column[this_row + 1:trees_y]
        left = trees[this_row][:this_tree]
        right = trees[this_row][this_tree + 1:trees_y]

        # up and left needs special care, because the ordering matters this time
        up = list(reversed(up))
        left = list(reversed(left))
        trees_around_me = [up, down, left, right]

        # Calculate scenic score for my tree
        scenic_score = 1
        for direction in trees_around_me:
            scenic_score *= I_see_x_trees(direction, this_tree_height)

        # If scenic score is higher than the winner, update highest_scenic_score
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

        # Move on to the next tree
        this_tree += 1

    # Move on to the next row of trees
    this_row += 1

print(f"The highest scenic score for any given tree is {highest_scenic_score}.")
