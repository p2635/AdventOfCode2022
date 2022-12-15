test_string = "30373\n25512\n65332\n33549\n35390"

# This challenge is about counting visible trees
visible_trees = 0

# Create 2D array
with open("input/d8.txt", mode = "r") as input:    
    file = [line.strip() for line in input]

# Output data about the text file
rows = len(file)
columns = len(file[0])
print(f"There are {rows} rows and {columns} columns.")

# If it's the first or last row/column, then those trees are visible by default
edge_trees = 2*(rows + columns) - 4
visible_trees += edge_trees
print(f"Around the edge, there are {visible_trees} visible trees.")

# Indexes to start counting from (only the inside, not the edge)
start = 1
end_row = rows - 1
end_column = columns - 1

# Give a tree and a list of trees, determine if it is visible

# A tree is visible if it is tallest in any direction
# a = print(is_tallest(3, [7, 3]))
