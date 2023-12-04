# f = open('day3input.txt', 'r')
f = open('day3sample.txt', 'r')
map = f.read().split('\n')

nums = '1234567890'
symbols = '@#$%&*'

num_table = []
sym_table = set()

for y in range(len(map)):
    for x in range(len(map[0])):
        print(map[y][x])

