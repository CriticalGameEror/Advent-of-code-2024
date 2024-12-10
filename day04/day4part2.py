import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

a_locations = set()
for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] == "A":
            a_locations.add((y, x))

m_locations = set()
s_locations = set()
# loops through all 'A's and checks surrounding characters for an S, finding if the opposite cords relates to an 'M', meaning 'MAS' has been found
for location in a_locations:
    y, x = location
    for y_addition in range(-1, 2):
        for x_addition in range(-1, 2):
            if (x == 0 and x_addition == -1) or (x == len(input_text[y])-1 and x_addition == 1) or (y == 0 and y_addition == -1) or (y == len(input_text)-1 and y_addition == 1):
                continue
            if input_text[y+(y_addition)][x+(x_addition)] == "S" and (y-(y_addition) >= 0 and y-(y_addition) <= len(input_text)-1) and (x-(x_addition) >= 0 and x-(x_addition) <= len(input_text[y])-1):
                if input_text[y-(y_addition)][x-(x_addition)] == "M":
                    s_locations.add((y+(y_addition), x+(x_addition)))
                    m_locations.add((y-(y_addition), x-(x_addition)))

total = 0
# loops through all 'A's and checks if the 4 adjacent spaces where an M and S should be
for location in a_locations:
    y, x = location
    # I know below is really ugly but I needed a quick and dirty solution
    if ((y-1, x-1) in m_locations and (y-1, x+1) in m_locations and (y+1, x-1) in s_locations and (y+1, x+1) in s_locations) or ((y-1, x-1) in s_locations and (y-1, x+1) in s_locations and (y+1, x-1) in m_locations and (y+1, x+1) in m_locations) or ((y-1, x-1) in m_locations and (y+1, x-1) in m_locations and (y-1, x+1) in s_locations and (y+1, x+1) in s_locations) or ((y-1, x-1) in s_locations and (y+1, x-1) in s_locations and (y-1, x+1) in m_locations and (y+1, x+1) in m_locations):
        total += 1
print(total)
