with open('day1part1_input.txt', 'r') as f:
    instructions = [line.strip() for line in f]

dial_value = 50
zero_count = 0

for instruction in instructions:
    operation = instruction[0]
    number = int(instruction[1:])
    
    if operation == 'R':
        new_value = dial_value + number
        zero_count += new_value // 100
        dial_value = new_value % 100
            
    elif operation == 'L':
        new_value = dial_value - number
        zero_count += -(new_value // 100)
        dial_value = new_value % 100

print("Total times dial hit + crossed zero:", zero_count)