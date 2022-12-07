with open("input/d6.txt", encoding='utf-8', mode="r") as file:
    signal = file.read().strip()

print(f"The length of the text file is {len(signal)}")

def check_repeating_chars(string):
    for i in string:
        if string.count(i) > 1:
            return True
    return False

def comm_system(process_chunk_size):
    i = 0
    while i in range(len(signal)):
        chunk = signal[i:i + process_chunk_size]
        # If chunk is less than 4, exit.
        if len(chunk) < process_chunk_size:
            break
        elif check_repeating_chars(chunk) == False:
            # Check first marker
            return (i + process_chunk_size)
        i += 1

# Part 1
# print(f"Part 1 - The number of markers is {comm_system(4)}")

# Previous attempts
# - 1964 too high
# - 496 too low
# Correct: 1262
# Lesson learned, read the question carefully

# Part 2
print(f"Part 2 - The number of markers is {comm_system(14)}")
