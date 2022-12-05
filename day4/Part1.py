####################################################
## Day 4 (Part 1) - The camp cleanup event
####################################################

overlap = 0 # the overlap count

# Data handling
with open("input/d4.txt", encoding="utf-8", mode="r") as file:
    # Clean \n characters
    camp_pairs = [pair.strip() for pair in file]

# OK OK, all elf pairs line up, let's see who is overlapping here!
for string in camp_pairs:

    ##################################################
    # MAKING THE ELF MACHINE SCANNER WORK
    ##################################################

    # Given a string '1-4,22-49', split it to a list ['1-4', '22,49']
    elf_pair = string.split(',')

    # Duplicate code here, think about refactoring!!
    # Given a string '1-4' or '22-49', split it to a list ['1','4'] ['22','49']
    elf1 = elf_pair[0].split('-')
    elf2 = elf_pair[1].split('-')

    # Convert to int
    elf1 = [int(assignment) for assignment in elf1]
    elf2 = [int(assignment) for assignment in elf2]

    # Get a list of the full areas that the elf is assigned
    # Given one assignment [1,4] or [22,49], convert it to a set of numbers {1,2,3,4}
    elf1 = {number for number in range(elf1[0], elf1[1] + 1)}
    elf2 = {number for number in range(elf2[0], elf2[1] + 1)}

    ##################################################
    # USING THE ELF MACHINE SCANNER
    ##################################################

    print("===== ANALYSING PAIR ======")
    print(f"Elf 1 has the assigned areas: {elf1}")
    print(f"Elf 2 has the assigned areas: {elf2}")

    # If either party have done the counterpart's work, mark it down.
    if elf1.intersection(elf2) == elf2 or elf2.intersection(elf1) == elf1:
        print("There is overlap:")
        print(elf1.intersection(elf2))
        overlap += 1
    else:
    # Otherwise, do nothing.
        print("There is no overlap.")

    # Move on to the next elf pair
    print("====== NEXT PAIR. ======")

# The conclusion of the event.
print(f"===== CONCLUSION =====\nThere are {overlap} overlaps for camp cleanup work.")
