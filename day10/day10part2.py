import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]


def find_sorrounding(find_number: int, current_cord: tuple[int, int], coords: dict):
    cord_list = []
    for y_addition in (-1, 0, 1):
        for x_addition in (-1, 0, 1):
            # below excludes diagonals
            if abs(y_addition) == abs(x_addition):
                continue
            elif (current_cord[0]+y_addition, current_cord[1]+x_addition) in coords[find_number]:
                cord_list.append(
                    (current_cord[0]+y_addition, current_cord[1]+x_addition, find_number))
    return cord_list


# the code block below gets all coords that each number appears at
coords_dict = {}
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] == ".":
            continue
        current_numb = int(input_text[y][x])
        if current_numb not in coords_dict:
            coords_dict[current_numb] = set()
        coords_dict[current_numb].add((y, x))

total = 0
lookup_queue = []
# goes through each trailhead
for start_cord in coords_dict[0]:
    visited_locations = set()
    lookup_queue += find_sorrounding(1, start_cord, coords_dict)
    while len(lookup_queue) != 0:
        current_lookup = lookup_queue.pop()
        if current_lookup[2] == 9:
            total += 1
        else:
            lookup_queue += find_sorrounding(
                current_lookup[2]+1, (current_lookup[0], current_lookup[1]), coords_dict)
print(total)
