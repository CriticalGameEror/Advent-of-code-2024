import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename) as f:
    input_text = f.readlines()
    for x in range(len(input_text)):
        input_text[x] = input_text[x].strip()

left_list = []
right_list = []
for x in input_text:
    split_list = x.split("   ")
    left_list.append(int(split_list[0]))
    right_list.append(int(split_list[1]))
left_list.sort()
right_list.sort()

total = 0
for x in left_list:
    total += (right_list.count(x) * x)
print(total)
