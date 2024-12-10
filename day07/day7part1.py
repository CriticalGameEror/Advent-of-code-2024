import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip().split(" ") for x in f.readlines()]


def calculate(current_total, target_total, current_list, current_index):
    # if all items in the list have been gone through and its equal to the total
    if current_total == target_total and current_index == len(current_list):
        return True
    # else if the current total is more than the target or it has reached the end of the list without matching the total
    elif current_total > target_total or current_index == len(current_list):
        return False
    elif calculate(current_total+int(current_list[current_index]),
                   target_total, current_list, current_index+1):
        return True
    elif calculate(current_total*int(current_list[current_index]),
                   target_total, current_list, current_index+1):
        return True
    return False


total = 0
for line in input_text:
    if calculate(0, int(line[0].strip(":")), line, 1):
        total += int(line[0].strip(":"))
print(total)
