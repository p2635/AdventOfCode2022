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

    string = commands[i]

    # Navigate folders for cd
    if "$ cd .." == string:
        navi.go_up_a_folder()
    elif "$ cd" in string:
        dir_name = string.replace("$ cd ", "")
        navi.go_down_a_folder(dir_name)

    # if starts with number, add the file to current dir
    elif is_file(string):
        split = string.split()
        navi.add_file(name = split[1], size = int(split[0]))

    # if starts with 'dir', add the folder to current dir
    elif is_dir(string):
        split = string.split()
        navi.add_folder(name = split[1])

    i += 1

## CHECK THE STRUCTURE ##
navi.print_directory_structure(navi.active_folder)

### UPDATING FOLDERS WITH THE FOLDER SIZE INFORMATION ###

navi.go_up_to_root()
navi.update_folder_sizes()
navi.go_up_to_root()

## No idea if I have done this update process right, moving to part 1.

### PART 1 - FILTER AND SUM FOLDERS < 100K ELF BYTES ###

print(navi.report_on_part1(navi.active_folder))
