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
seconds = 0
easter_egg_found = False
while not easter_egg_found:
    seconds += 1
    final_positions = set()
    for robot in robots:
        final_positions.add(find_final_position(
            (robot[0], robot[1]), (robot[2], robot[3]), seconds, x_bound, y_bound))
    for position in final_positions:
        # below checks for a large number of robots in a straight vertical line (the picture border)
        if all(((position[0], position[1]-x) in final_positions for x in range(20))):
            print(seconds)
            easter_egg_found = True
            break
