import os
import re

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

total = 0
all_instructions = []
for line in input_text:
    all_instructions += re.findall(
        r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
for multiply in all_instructions:
    split_list = multiply.split(",")
    total += int(split_list[0].strip("mul(")) * int(split_list[1].strip(")"))
print(total)
