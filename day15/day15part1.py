import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

boxes = set()
robot = ()
walls = set()
directions = ""
for y in range(len(input_text)):
    if input_text[y] == "":
        directions = "".join(input_text[y+1:])
        break
    for x in range(len(input_text[y])):
        item = input_text[y][x]
        match item:
            case "@":
                robot = (y, x)
            case "#":
                walls.add((y, x))
            case "O":
                boxes.add((y, x))

direction_values = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for direction in directions:
    future_robot_position = (robot[0] + direction_values[direction][0],
                             robot[1] + direction_values[direction][1])
    if future_robot_position in boxes:
        base_addition = (
            direction_values[direction][0], direction_values[direction][1])
        incrementer = 1
        current_offset = (robot[0]+(base_addition[0]*incrementer),
                          robot[1]+(base_addition[1]*incrementer))
        while current_offset in boxes:
            incrementer += 1
            current_offset = (robot[0]+(base_addition[0]*incrementer),
                              robot[1]+(base_addition[1]*incrementer))
        if current_offset in walls:
            continue
        else:
            incrementer -= 1
            while incrementer > 0:
                current_offset = (
                    robot[0]+base_addition[0]*incrementer, robot[1]+base_addition[1]*incrementer)
                boxes.remove(current_offset)
                boxes.add((robot[0]+base_addition[0]*(incrementer+1),
                          robot[1]+base_addition[1]*(incrementer+1)))
                incrementer -= 1

            robot = future_robot_position
    elif future_robot_position not in walls:
        robot = future_robot_position

total = 0
for box in boxes:
    total += (100 * box[0] + box[1])
print(total)
