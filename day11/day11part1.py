import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readline().strip().split(" ")


total = 0
blink_count = 25  # change this depending on blink requirement
for stone in input_text:
    current_list = [int(stone)]
    for blink in range(blink_count):
        new_list = []
        for item in current_list:
            if item == 0:
                new_list.append(1)
            elif len(str(item)) % 2 == 0:
                new_list.append(int(str(item)[:int(len(str(item))/2)]))
                new_list.append(int(str(item)[int(len(str(item))/2):]))
            else:
                new_list.append(item * 2024)
            current_list = new_list.copy()
    total += len(current_list)
print(total)
