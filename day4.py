f = open("day4input.txt", 'r')
# f = open("day4sample.txt", 'r')
# f = open("day4sample2.txt", 'r')
lines = f.readlines()

import re

total_points = 0
for line in lines:
    card_match = re.search(r'Card(\ +)(\d+):', line)
    card_no = int(card_match.group(2))
    line = re.sub(r'Card(\ +)(\d+):', '', line)
    tickets = line.split('|')
    match = 0
    for num in [int(_) for _ in tickets[1].strip().split()]:
        if num in [int(_) for _ in tickets[0].strip().split()]:
            match += 1
        points = 0 if match == 0 else 2 ** (match - 1)
    total_points += points

print(total_points)

# Part 2

cards = []
for line in lines:
    parts = re.split(r'\||:', line)
    winning_numbers = set(map(int, parts[1].strip().split()))
    drawn_numbers = set(map(int, parts[2].strip().split()))
    cards.append((winning_numbers, drawn_numbers))

card_counts = {i: 1 for i in range(len(cards))}
total_cards = 0

for i, (winning, drawn) in enumerate(cards):
    matches = len(winning & drawn)
    total_cards += card_counts[i]

    for j in range(i + 1, min(i + 1 + matches, len(cards))):
        card_counts[j] += card_counts[i]

print(total_cards)