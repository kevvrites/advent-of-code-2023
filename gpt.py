import re

def parse_schematic(schematic):
    numbers = []
    for y, row in enumerate(schematic):
        for match in re.finditer(r'\d+', row):
            numbers.append(((y, match.start()), match.group()))
        print(numbers)
        return numbers

def is_adjacent_to_symbol(schematic, number_position, number_str):
    y, x = number_position
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(schematic) and 0 <= nx < len(schematic[0]):
                if schematic[ny][nx] in '@#$%&*-=':
                    return True
            
        if len(number_str) > 1:
            for i in range(1, len(number_str)):
                if schematic[y][x + i] in '@#$%&*-=':
                    return True
        return False
    
def sum_part_numbers(schematic):
    numbers = parse_schematic(schematic)
    total = 0
    for position, number_str in numbers:
        if is_adjacent_to_symbol(schematic, position, number_str):
            total += int(number_str)
    return total

schematic = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

print(sum_part_numbers(schematic))