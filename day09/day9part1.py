import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readline().strip()


disk = []
current_space_index = 0
for digit in range(len(input_text)):
    digit = int(digit)
    if digit % 2 == 0:
        disk += [int(digit)/2] * int(input_text[digit])
        current_space_index += int(input_text[digit])
    else:
        if int(input_text[digit]) != 0:
            disk += ["."] * int(input_text[digit])

left_pointer = 0
right_pointer = len(disk)-1
while left_pointer != right_pointer:
    if disk[left_pointer] != ".":
        left_pointer += 1
        continue
    if disk[right_pointer] == ".":
        right_pointer -= 1
        continue
    disk[left_pointer], disk[right_pointer] = disk[right_pointer], disk[left_pointer]

total = 0
for index, value in enumerate(disk):
    if value == ".":
        break
    total += (index * value)
print(int(total))
