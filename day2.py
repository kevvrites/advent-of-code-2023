import re

f = open("day2input.txt", 'r')
# f = open("day2sample.txt", 'r')
lines = f.readlines()

# Part 1 & 2
sum_id = 0
total_power = 0

for line in lines:
    mr = 0
    mg = 0
    mb = 0
    game_id_match = re.search(r'Game (\d+):', line)
    game_id = int(game_id_match.group(1))
    segments = line.split(';')
    for segment in segments:
        red_count = re.search(r'(\d+) red', segment)
        blue_count = re.search(r'(\d+) blue', segment)
        green_count = re.search(r'(\d+) green', segment)

        red = int(red_count.group(1)) if red_count else 0
        blue = int(blue_count.group(1)) if blue_count else 0
        green = int(green_count.group(1)) if green_count else 0
        if red > mr:
            mr = red
        if green > mg:
            mg = green
        if blue > mb:
            mb = blue
        power = mr * mg * mb
    total_power += power
    if mr <= 12 and mg <= 13 and mb <= 14:
        sum_id += game_id

print(sum_id) # part 1 solution
print(total_power) # part 2 solution