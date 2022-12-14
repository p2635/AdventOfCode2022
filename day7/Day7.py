from Parser import is_file, is_dir
from Navigator import Navigator
from Items import Folder

# The main stuff

with open("input/d7.txt", encoding='utf-8', mode="r") as file:
    commands = [line.strip() for line in file]

### BUILDING THE FILE/FOLDER STRUCTURE ###

i = 1 # Skip the first line of cd /
navi = Navigator(Folder("/")) # New navigator starts at /

while i < len(commands):

    line = commands[i]

    # Navigate folders for cd

    if "$ cd .." == line:
        navi.go_up_a_folder()

    elif "$ cd" in line:
        dir_name = line.replace("$ cd ", "")
        navi.go_down_a_folder(dir_name)

    # if starts with number, add the file to current dir
    elif is_file(line):
        split = line.split()
        navi.add_file(name = split[1], size = int(split[0]))

    # if starts with 'dir', add the folder to current dir
    elif is_dir(line):
        split = line.split()
        navi.add_folder(name = split[1])

    i += 1

### UPDATING FOLDERS WITH THE FOLDER SIZE INFORMATION ###
navi.go_up_to_root()
navi.update_folder_sizes()

## No idea if I have done this update process right, moving to part 1.

## CHECK THE STRUCTURE ##
navi.go_up_to_root()
navi.print_directory_structure(navi.active_folder)

### PART 1 - FILTER AND SUM FOLDERS < 100K ELF BYTES ###
print(navi.report_on_part1(navi.active_folder))

# Failed guesses: 2915238 and others that I don't remember

### PART 2 - FILTER AND SUM FOLDERS < 100K ELF BYTES ###
print(f">>>> It's time for part 2 <<<<")
print(f" - Total Size of root \ is {navi.total_disk_space:,}.")
print(f" - At the moment, we have {navi.calc_unused_space():,} free space.")
print(f" - The update requires {navi.required_update_space:,}.")
print(f" - Is this enough space? System: {navi.is_enough_space()}.")

space_to_free_up = navi.required_update_space - navi.calc_unused_space()
print(f" - How much do we need to free up then? System: {space_to_free_up:,}.")

print(f">>>> Searching... <<<<")
print(navi.report_on_part2(navi.root_folder))
