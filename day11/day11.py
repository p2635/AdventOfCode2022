from Monkey import Monkey

rounds = 20

# with open("input/d11.txt", "r") as file:
#     monkey_instructions = [line.strip() for line in file]

m1 = Monkey([79, 98], "* 19")

m1.inspect_items()

print(m1.inspect_count)

# m2 = Monkey("old * 19", [56, 34])

# print(m1.items, m2.items)
# m1.throw(m2)
# print(m2.items)
