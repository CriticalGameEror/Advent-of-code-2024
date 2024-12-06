import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

GAURD_ROTATIONS = ("^", ">", "v", "<")
positions = {}
gaurd_rotation = 0
gaurd_position = 0
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] == "#":
            positions[(y, x)] = "#"
        elif input_text[y][x] in GAURD_ROTATIONS:
            gaurd_position = (y, x)
            gaurd_rotation = GAURD_ROTATIONS.index(input_text[y][x])

gaurd_off_map = False
visited_location = set()
while gaurd_off_map is False:
    x_addition = 0
    y_addition = 0
    match GAURD_ROTATIONS[gaurd_rotation]:
        case "^":
            y_addition = -1
        case ">":
            x_addition = 1
        case "v":
            y_addition = 1
        case "<":
            x_addition = -1
    while gaurd_position[0] >= 0 and gaurd_position[0] < len(input_text) and gaurd_position[1] >= 0 and gaurd_position[1] < len(input_text[0]):
        visited_location.add((gaurd_position[0], gaurd_position[1]))
        new_position = (gaurd_position[0]+y_addition,
                        gaurd_position[1]+x_addition)
        if new_position in positions:
            gaurd_rotation = (gaurd_rotation+1) % 4
            break
        else:
            gaurd_position = new_position
    else:
        gaurd_off_map = True
print(len(visited_location))
