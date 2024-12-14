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
                        (int(button2_left), int(button2_right)), (int(temp1), int(temp2))])

total = 0
for machine in machine_list:
    lowest_tokens = -1
    for a_button in range(101):
        for b_button in range(101):
            if ((machine[0][0]*a_button)+(machine[1][0]*b_button), (machine[0][1]*a_button)+(machine[1][1]*b_button)) == machine[2]:
                if (a_button*3) + b_button < lowest_tokens or lowest_tokens == -1:
                    lowest_tokens = (a_button*3) + b_button
    if lowest_tokens != -1:
        total += lowest_tokens
print(total)
