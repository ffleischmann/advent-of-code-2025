with open('day1part1_input.txt', 'r') as f:
    instructions = [line.strip() for line in f]

dial_value = 50
zero_count = 0

for instruction in instructions:
    operation = instruction[0]
    number = int(instruction[1:])
    
    if operation == 'R':
        old_value = dial_value
        new_value = dial_value + number
        dial_value = new_value % 100
        
        # Count multiples of 100 in range (old_value, new_value]
        zero_count += new_value // 100 - old_value // 100
            
    elif operation == 'L':
        old_value = dial_value
        new_value = dial_value - number  
        dial_value = new_value % 100
        
        zero_count += (old_value - 1) // 100 - (new_value - 1) // 100

print("Total times dial hit + crossed zero:", zero_count)