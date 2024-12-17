import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = [x.strip() for x in f.readlines()]

register_A = int(input_text[0].strip("Register A:"))
register_B = int(input_text[1].strip("Register B:"))
register_C = int(input_text[2].strip("Register C:"))
instructions = [int(x) for x in input_text[4].strip("Program: ").split(",")]
instruction_pointer = 0


def divide(numerator, denominator):
    temp = str(numerator / (2**denominator))
    return int(temp.split(".")[0])


def get_combo_value(combo_number, register_a, register_b, register_c):
    match combo_number:
        case 0 | 1 | 2 | 3:
            combo_value = combo_number
        case 4:
            combo_value = register_a
        case 5:
            combo_value = register_b
        case 6:
            combo_value = register_c
        case _:
            raise ValueError("7 should not appear in valid programs")
    return combo_value


output = []
while instruction_pointer < len(instructions):
    match instructions[instruction_pointer]:
        case 0:
            combo_value = get_combo_value(
                instructions[instruction_pointer+1], register_A, register_B, register_C)
            register_A = divide(register_A, combo_value)
        case 1:
            register_B ^= instructions[instruction_pointer+1]
        case 2:
            register_B = combo_value = get_combo_value(
                instructions[instruction_pointer+1], register_A, register_B, register_C) % 8
        case 3:
            if register_A != 0:
                instruction_pointer = instructions[instruction_pointer+1]
                continue
        case 4:
            register_B ^= register_C
        case 5:
            output.append(str(get_combo_value(
                instructions[instruction_pointer+1], register_A, register_B, register_C) % 8))
        case 6:
            combo_value = get_combo_value(
                instructions[instruction_pointer+1], register_A, register_B, register_C)
            register_B = divide(register_A, combo_value)
        case 7:
            combo_value = get_combo_value(
                instructions[instruction_pointer+1], register_A, register_B, register_C)
            register_C = divide(register_A, combo_value)
    instruction_pointer += 2
print(",".join(output))
