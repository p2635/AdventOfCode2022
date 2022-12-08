from Navigator import Navigator
from Items import Folder

def is_command(string):
    return '$' in string

with open("input/d7.txt", encoding='utf-8', mode="r") as file:
    commands = [line.strip() for line in file]

i = 1 # Skip the first line of cd /
navi = Navigator(Folder("/")) # New navigator starts at /
while i < len(commands):
    if  commands[i]:
        print(commands[i])
    i += 1

# Given a string, determine if it's a file or folder
# '24836 rsjcg.lrh'
# 'dir vrj'
def parse_ls(string):
    # if starts with number, return an object that with file_size, name, and file type of 'file'
    # if starts with 'dir', return an object that with file_size (if known), name, and file type of 'folder'
    pass

