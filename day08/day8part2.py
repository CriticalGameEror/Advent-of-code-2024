import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

# stores the antenna positions
antenna_positions = {}

for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] != ".":
            if input_text[y][x] not in antenna_positions:
                antenna_positions[input_text[y][x]] = set()
                antenna_positions[input_text[y][x]].add((y, x))
            else:
                antenna_positions[input_text[y][x]].add((y, x))

antinode_positions = set()
for antenna in antenna_positions:
    for current_location in antenna_positions[antenna]:
        for looked_location in antenna_positions[antenna]:
            if current_location == looked_location:
                continue
            looped_position = current_location
            out_of_map = False
            while out_of_map is False:
                antinode_position = (
                    looped_position[0] + (looked_location[0] - current_location[0]), looped_position[1] + (looked_location[1] - current_location[1]))
                if antinode_position[0] < 0 or antinode_position[0] >= len(input_text) or antinode_position[1] < 0 or antinode_position[1] >= len(input_text[0]):
                    out_of_map = True
                    continue
                antinode_positions.add(antinode_position)
                looped_position = antinode_position
print(len(antinode_positions))
