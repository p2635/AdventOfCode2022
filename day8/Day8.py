string = "30373\n25512\n65332\n33549\n35390"

print(string)

with open("input/d8.txt", mode = "r") as input:
    for line in input:
        print(line.strip())

# Give a tree and a list of trees, determine if it is visible
# This does not care about the ordering of the trees list
def is_tallest(specific_tree, trees):

    if trees == []:
        # If it's an edge tree, then it's visible
        return True
    else:
        # Otherwise go through every tree
        for tree in trees:
            if tree > specific_tree:
                return False

    # If you've gone through every tree, it must be visible
    return True

# A tree is visible if it is tallest in any direction
# a = print(is_tallest(3, [7, 3]))
