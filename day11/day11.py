import re, copy
from Monkey import Monkey

##############################################################################
##           Parsing the text file to get a list of monkeys
##############################################################################
original_monkeys = []

with open("input/d11.txt", "r") as file:
    monkey_instructions = [line.strip() for line in file]

# To workaround the problem of the word 'old' conflict with my var name 'item'
for i in range(len(monkey_instructions)):
    monkey_instructions[i] = monkey_instructions[i].replace("old", "item")

# For each monkey in the text file, create a new monkey and put it in a monkeys list
for i in range(0, len(monkey_instructions), 7): # Each monkey is 7 lines in input.txt

    # For log's sake
    print("== ADDING MONKEY TO A LIST ==")
    print(monkey_instructions[i])

    # Get all the information
    items = [int(s) for s in re.findall(r'\d+', monkey_instructions[i + 1])]
    operation = monkey_instructions[i + 2].split("Operation: new = ", 1)[1]
    test = int(re.findall(r'\d+', monkey_instructions[i + 3])[0]) # [0] first element to avoid list data type
    m1 = int(re.findall(r'\d+', monkey_instructions[i + 4])[0])
    m2 = int(re.findall(r'\d+', monkey_instructions[i + 5])[0])
    print(items, operation, test, m1, m2, sep="\n")

    # Create a new monkey and add to the list
    original_monkeys.append(Monkey(items, operation, test, m1, m2))

##############################################################################
##           Part 1 of the puzzle
##############################################################################
print("===== PART 1 BEGINS =====")

rounds = 20
part1_monkeys = copy.deepcopy(original_monkeys)
for i in range(rounds):
    
    print(f"===== ROUND {i + 1} =====")
    # For monkey in monkeys, inspect item and throw stuff
    for i in range(len(part1_monkeys)):

        current_monkey = part1_monkeys[i]
        print(f"Monkey {i}:")

        if len(current_monkey.items) == 0:
            print("\tNo action, the monkey has no items.")
            continue

        print(f"> Current Items: {current_monkey.items}")
   
        while len(current_monkey.items) != 0:
            
            # Monkey inspects (always the first item, since it keeps throwing items)
            print(f"\tMonkey inspects item with worry level {current_monkey.items[0]}.")
            current_monkey.items[0] = current_monkey.inspect(current_monkey.items[0])
            print(f"\t\tWorry level is {current_monkey.operation} to {current_monkey.items[0]}.")

            # Monkey gets bored
            new_value = current_monkey.get_bored(current_monkey.items[0], 3)
            print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {new_value}.")
            current_monkey.items[0] = new_value
            
            # Division test
            result = current_monkey.divitest_item(current_monkey.items[0])
            if result:
                monkey_to_catch = current_monkey.target_monkey1
            else:
                monkey_to_catch = current_monkey.target_monkey2 
            print(f"\t\tCurrent worry level is divisible by {current_monkey.divi_test}: {result}")
            
            # Monkey throws for the first item
            print(f"\t\tItem with worry level {current_monkey.items[0]} is thrown to Monkey {monkey_to_catch}.")
            current_monkey.throw_first_item(part1_monkeys[monkey_to_catch])

            # Monkey keeps track of how many times he inspects
            current_monkey.inspect_count += 1

print("===== Inspect counts =====")
for i in range(len(part1_monkeys)):
    print(f"* Monkey {i} inspected items {part1_monkeys[i].inspect_count} times.")

##############################################################################
##           Part 2 of the puzzle
##           same thing, only difference is more rounds and no dividing
##############################################################################
print("===== PART 2 BEGINS =====")

rounds = 10000
part2_monkeys = copy.deepcopy(original_monkeys)

for i in range(rounds):
    
    # print(f"===== ROUND {i + 1} =====")
    # For monkey in monkeys, inspect item and throw stuff
    for i in range(len(part2_monkeys)):

        current_monkey = part2_monkeys[i]
        # print(f"Monkey {i}:")

        if len(current_monkey.items) == 0:
            # print("\tNo action, the monkey has no items.")
            continue

        # print(f"> Current Items: {current_monkey.items}")
   
        while len(current_monkey.items) != 0:
            
            # Monkey inspects (always the first item, since it keeps throwing items)
            # print(f"\tMonkey inspects item with worry level {current_monkey.items[0]}.")
            current_monkey.items[0] = current_monkey.inspect(current_monkey.items[0])
            # print(f"\t\tWorry level is {current_monkey.operation} to {current_monkey.items[0]}.")

            # Monkey gets bored
            new_value = current_monkey.get_bored(current_monkey.items[0], 4)
            # print(f"\t\tMonkey gets bored with item. Worry level is divided by 4 to {new_value}.")
            current_monkey.items[0] = new_value
            
            # Division test
            result = current_monkey.divitest_item(current_monkey.items[0])
            if result:
                monkey_to_catch = current_monkey.target_monkey1
            else:
                monkey_to_catch = current_monkey.target_monkey2 
            # print(f"\t\tCurrent worry level is divisible by {current_monkey.divi_test}: {result}")
            
            # Monkey throws for the first item
            # print(f"\t\tItem with worry level {current_monkey.items[0]} is thrown to Monkey {monkey_to_catch}.")
            current_monkey.throw_first_item(part2_monkeys[monkey_to_catch])

            # Monkey keeps track of how many times he inspects
            current_monkey.inspect_count += 1

    for i in part2_monkeys:
        print(i.items)

print("===== Inspect counts =====")
for i in range(len(part2_monkeys)):
    print(f"* Monkey {i} inspected items {part2_monkeys[i].inspect_count} times.")
