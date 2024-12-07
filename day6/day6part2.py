import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]


def traverse(obstacle_positions: set[tuple[int, int]], gaurd_position: tuple[int, int, int]) -> set[tuple[int, int]] | bool:
    gaurd_off_map = False
    in_loop = False
    visited_location = set()
    # an additional set is needed to keep track of loops, the first set must only track location and not rotation to avoid duplicates
    visited_location_wrotation = set()
    while gaurd_off_map is False and in_loop is False:
        x_addition = 0
        y_addition = 0
        match GAURD_ROTATIONS[gaurd_position[2]]:
            case "^":
                y_addition = -1
            case ">":
                x_addition = 1
            case "v":
                y_addition = 1
            case "<":
                x_addition = -1
        while gaurd_position[0] >= 0 and gaurd_position[0] < len(input_text) and gaurd_position[1] >= 0 and gaurd_position[1] < len(input_text[0]):
            if (gaurd_position[0], gaurd_position[1], gaurd_position[2]) in visited_location_wrotation:
                in_loop = True
                break
            visited_location.add((gaurd_position[0], gaurd_position[1]))
            visited_location_wrotation.add(
                (gaurd_position[0], gaurd_position[1], gaurd_position[2]))
            new_position = (gaurd_position[0]+y_addition,
                            gaurd_position[1]+x_addition)
            if new_position in obstacle_positions:
                gaurd_position = (
                    gaurd_position[0], gaurd_position[1], (gaurd_position[2]+1) % 4)
                break
            else:
                gaurd_position = (
                    new_position[0], new_position[1], gaurd_position[2])
        else:
            gaurd_off_map = True
    return visited_location, in_loop


GAURD_ROTATIONS = ("^", ">", "v", "<")
positions = set()
# stores y and x position and the index of the rotation
gaurd_position = 0
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] == "#":
            positions.add((y, x))
        elif input_text[y][x] in GAURD_ROTATIONS:
            gaurd_position = (y, x, GAURD_ROTATIONS.index(input_text[y][x]))


visited_locations = traverse(positions, gaurd_position)[0]
total = 0
for location in visited_locations:
    temp_positions = positions.copy()
    temp_positions.add(location)
    if traverse(temp_positions, gaurd_position)[1] is True:
        total += 1
print(total)
