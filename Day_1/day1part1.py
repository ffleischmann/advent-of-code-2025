with open('day1part1_input.txt', 'r') as f:
    instructions = [line.strip() for line in f]

dial_value = 50
zero_count = 0

for instruction in instructions:
    operation = instruction[0]
    number = int(instruction[1:])
    if operation == 'R':
        dial_value = (dial_value + number) % 100
    elif operation == 'L':
        dial_value = (dial_value - number) % 100

    if dial_value == 0:
        zero_count += 1

print("Total times dial hit zero:", zero_count)