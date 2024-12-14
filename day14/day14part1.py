import os
import math

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

# stores the position x,y and then the velocity x, y
robots = []
for line in input_text:
    position, velocity = line.split(" ")
    position, velocity = position.strip("p=").split(
        ","), velocity.strip("v=").split(",")
    robots.append((int(position[0]), int(position[1]),
                  int(velocity[0]), int(velocity[1])))


def find_final_position(current_position, velocity, seconds, grid_x_bound, grid_y_bound):
    return ((current_position[0] + (velocity[0] * seconds)) %
            grid_x_bound, (current_position[1] + (velocity[1] * seconds)) % grid_y_bound)


x_bound = 101
y_bound = 103
final_positions = []
for robot in robots:
    final_positions.append(find_final_position(
        (robot[0], robot[1]), (robot[2], robot[3]), 100, x_bound, y_bound))

# stored quadrants going left to right, up to down
quadrants = [None, None, None, None]
for position in final_positions:
    middle_x, middle_y = int(x_bound/2), int(y_bound/2)
    if position[0] < middle_x and position[1] < middle_y:
        if quadrants[0] is None:
            quadrants[0] = 0
        quadrants[0] += 1
    elif position[0] > middle_x and position[1] < middle_y:
        if quadrants[1] is None:
            quadrants[1] = 0
        quadrants[1] += 1
    elif position[0] < middle_x and position[1] > middle_y:
        if quadrants[2] is None:
            quadrants[2] = 0
        quadrants[2] += 1
    elif position[0] > middle_x and position[1] > middle_y:
        if quadrants[3] is None:
            quadrants[3] = 0
        quadrants[3] += 1
print(math.prod(quadrants))
