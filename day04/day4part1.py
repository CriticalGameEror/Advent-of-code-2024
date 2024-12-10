import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

locations = set()
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] == "X":
            locations.add((y, x))

total = 0
# loops through each 'X' and checks 3 letters in every direction to check for a 'MAS', adding to the total if it is detected
for location in locations:
    y, x = location
    for y_addition in range(-1, 2):
        for x_addition in range(-1, 2):
            if (x < 3 and x_addition == -1) or (x > len(input_text[y])-4 and x_addition == 1) or (y < 3 and y_addition == -1) or (y > len(input_text)-4 and y_addition == 1):
                continue
            identified_letters = input_text[y+(y_addition)][x+(x_addition)] + input_text[y+(
                y_addition*2)][x+(x_addition*2)] + input_text[y+(y_addition*3)][x+(x_addition*3)]
            if identified_letters == "MAS":
                total += 1
print(total)
