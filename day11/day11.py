"""
Thanks to https://github.com/hugseverycat/aoc2024/blob/master/day11.py for a pointer on how to optimise for part 2
"""

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readline().strip().split(" ")


find_count_cache = {}


def find_count(current_numb, current_blink, required_blinks):
    if (current_numb, current_blink) in find_count_cache:
        return find_count_cache[(current_numb, current_blink)]
    if current_blink == required_blinks:
        return 1
    elif current_numb == 0:
        amount = find_count(1, current_blink+1, required_blinks)
    elif len(str(current_numb)) % 2 == 0:
        amount = find_count(int(str(current_numb)[:int(len(str(current_numb))/2)]), current_blink+1, required_blinks) + find_count(
            int(str(current_numb)[int(len(str(current_numb))/2):]), current_blink+1, required_blinks)
    else:
        amount = find_count(current_numb*2024,
                            current_blink+1, required_blinks)
    find_count_cache[(current_numb, current_blink)] = amount
    return amount


total = 0
blink_count = 75  # change this depending on blink requirement
blink_dict = {}
for stone in input_text:
    total += find_count(int(stone), 0, blink_count)
print(total)
