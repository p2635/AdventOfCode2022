def is_command(string):
    return '$' in string

with open("input/d7.txt", encoding='utf-8', mode="r") as file:
    commands = [line.strip() for line in file]

for line in commands:
    if is_command(line):
        pass # Should I use dictionaries? Map out what actions cd and ls do.

# Given a string, determine if it's a file or folder
# '24836 rsjcg.lrh'
# 'dir vrj'
def parse_ls(string):
    # if starts with number, return an object that with file_size, name, and file type of 'file'
    # if starts with 'dir', return an object that with file_size (if known), name, and file type of 'folder'
    pass

