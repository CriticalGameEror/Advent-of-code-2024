import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

machine_list = []
for line_index in range(0, len(input_text), 4):
    button1_left, button1_right = input_text[line_index].split(", Y+")
    button1_left = button1_left.strip("Button A: X+")
    button2_left, button2_right = input_text[line_index+1].split(", Y+")
    button2_left = button2_left.strip("Button B: X+")
    temp1, temp2 = input_text[line_index+2].split(", Y=")
    temp1 = temp1.strip("Prize: X=")
    machine_list.append([(int(button1_left), int(button1_right)),
                        (int(button2_left), int(button2_right)), (int(temp1)+10000000000000, int(temp2)+10000000000000)])

print(machine_list)