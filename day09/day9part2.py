import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readline().strip()


disk = []
# stores an ordered list of the index and the number of free spaces
free_space = []
# stores each file_id alongside its index and how big it is
file_ids = {}
current_space_index = 0
for digit in range(len(input_text)):
    digit = int(digit)
    if digit % 2 == 0:
        disk += [int(int(digit)/2)] * int(input_text[digit])
        file_ids[int(int(digit)/2)] = (current_space_index,
                                       int(input_text[digit]))
        current_space_index += int(input_text[digit])
    else:
        if int(input_text[digit]) != 0:
            free_space.append((current_space_index, int(input_text[digit])))
            current_space_index += int(input_text[digit])
            disk += ["."] * int(input_text[digit])


# goes from the highest file id to the lowest file id
for file_id in range(len(file_ids)-1, -1, -1):
    file = file_ids[file_id]
    # loops from the leftmost freespace to the rightmost freespace
    for space_index in range(len(free_space)):
        space = free_space[space_index]
        # breaks once the position of the next leftmost free space exceeds the current position of the file
        if space[0] > file[0]:
            break
        if space[1] >= file[1]:
            # loops for the space of the file
            for x in range(file[1]):
                # swaps the two spaces
                disk[space[0]+x] = file_id
                disk[file[0]+x] = "."
            # updates the freespace
            free_space[space_index] = (space[0]+file[1], space[1]-file[1])
            break

total = 0
for index, value in enumerate(disk):
    if value == ".":
        continue
    total += (index * value)
print(total)
