import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

letter_cords = {}
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] not in letter_cords:
            letter_cords[input_text[y][x]] = set()
        letter_cords[input_text[y][x]].add((y, x))


def findSorrounding(letter, current_position, checked_positions, cords_dict):
    for y_addition in (-1, 0, 1):
        for x_addition in (-1, 0, 1):
            if abs(y_addition) == abs(x_addition):
                continue
            checking_position = (
                current_position[0]+y_addition, current_position[1]+x_addition)
            if checking_position in cords_dict[letter] and checking_position not in checked_positions:
                checked_positions.add(checking_position)
                findSorrounding(letter, checking_position,
                                checked_positions, cords_dict)
    if len(checked_positions) == 0:
        checked_positions.add(current_position)
    return checked_positions


def gather_area_sides(locations):
    area = len(locations)
    sides = []
    for cord in locations:
        for y_addition in (-1, 0, 1):
            for x_addition in (-1, 0, 1):
                if abs(y_addition) == abs(x_addition):
                    continue
                if (cord[0]+y_addition, cord[1]+x_addition) not in locations:
                    sides.append((cord[0]+y_addition, cord[1]+x_addition))
    side_count = 0
    while len(sides) != 0:
        side = sides.pop(0)
        side_count += 1
        is_left_right = False
        right, left, up, down = 1, 1, 1, 1
        while (side[0], side[1]+right) in sides:
            sides.remove((side[0], side[1]+right))
            right += 1
            is_left_right = True
        while (side[0], side[1]-left) in sides:
            sides.remove((side[0], side[1]-left))
            left += 1
            is_left_right = True
        if not is_left_right:
            while (side[0]+down, side[1]) in sides:
                sides.remove((side[0]+down, side[1]))
                down += 1
            while (side[0]-up, side[1]) in sides:
                sides.remove((side[0]-up, side[1]))
                up += 1
    return area * side_count
    # while len(sides) != 0:
    #     side = sides.pop(0)
    #     side_count += 1
    #     is_left_right = False
    #     right, left, up, down = 1, 1, 1, 1
    #     while (side[0], side[1]+right) in sides:
    #         sides.remove((side[0], side[1]+right))
    #         right += 1
    #         is_left_right = True
    #     while (side[0], side[1]-left) in sides:
    #         sides.remove((side[0], side[1]-left))
    #         left += 1
    #         is_left_right = True
    #     if not is_left_right:
    #         while (side[0]+down, side[1]) in sides:
    #             sides.remove((side[0]+down, side[1]))
    #             down += 1
    #         while (side[0]-up, side[1]) in sides:
    #             sides.remove((side[0]-up, side[1]))
    #             up += 1
    # return area * side_count


total = 0
all_checked_positions = set()
for letter in letter_cords:
    for cord in letter_cords[letter]:
        if cord in all_checked_positions:
            continue
        returned_set = findSorrounding(
            letter, cord, set(), letter_cords)
        total += gather_area_sides(returned_set)
        all_checked_positions.update(returned_set)
print(total)
