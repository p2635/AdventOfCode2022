slot_size = 4 # Cargo 'slot' size in char length

# USE SLICING

def translate_row(str):
    # Read the string in blocks of three?
    # My first solution has a lot of specifying char lengths
    row = []
    for i in range(0, len(str), slot_size):
        row.append(str[i+1])
        # print(string[i:i+3])
    return row

with open("input/d5.txt", encoding='utf-8', mode="r") as file:

    # Store the original cargo map
    map = []
    for line in file:
        if line == "\n":
            break
        else:
            map.append(translate_row(line))
    
    # print(map)

    # print(list(zip(map)))