import TextFileParser
from CrateMover import CrateMover9k, CrateMover9k1

# First thing is to get the drawing of the stacks
# read line until you get to an empty line

with open("input/d5.txt", encoding='utf-8', mode="r") as file:

    # Store the original cargo map
    map = []
    for line in file:
        if "1" in line:
            break
        else:
            map.append(line.strip("\n"))

    # Put this map into Crate Mover 9000
    parsed_map = TextFileParser.translate_map(map)
    parsed_map2 = TextFileParser.translate_map(map)
    instructions = []
    cargo = CrateMover9k(parsed_map)

    # Start the processing
    for line in file:

        if "move" in line:

            # Store the 'move' instructions
            instructions.append(line)
            instruction = TextFileParser.parse_line_of_instruction(line)
            cargo.moveCargo(instruction)

        cargo.showCargo()

    # The answer to part 1
    print("The answer to part 1 is hopefully")
    cargo.showTopOfEachStack()

    # Put this map into Crate Mover 9001
    cargo = CrateMover9k1(parsed_map2)
    cargo.showCargo()

    # Start the processing
    for line in instructions:

        if "move" in line:
            instruction = TextFileParser.parse_line_of_instruction(line)
            cargo.moveCargo(instruction)

        cargo.showCargo()

    # The answer to part 2
    print("The answer to part 2 is hopefully")
    cargo.showTopOfEachStack()
