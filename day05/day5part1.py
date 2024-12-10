import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

# key is the number, the value is a set of all numbers that it should come before
come_before = {}
produced_page_index = 0
for line in input_text:
    if line == "":
        break
    num1, num2 = line.split("|")
    if num1 not in come_before:
        come_before[num1] = set()
    come_before[num1].add(num2)
    produced_page_index += 1

total = 0
for line in input_text[produced_page_index+1:]:
    number_list = line.split(",")
    list_broken = False
    for index, current_number in enumerate(number_list):
        if current_number not in come_before:
            continue
        for previous_number in number_list[:index]:
            if previous_number in come_before[current_number]:
                list_broken = True
                break
        if list_broken:
            break
        for future_number in number_list[index+1:]:
            if future_number not in come_before[current_number]:
                list_broken = True
                break
    if not list_broken:
        position = int((len(number_list)/2)-0.5)
        total += int(number_list[position])
print(total)
