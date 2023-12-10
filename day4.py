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

cards_to_process = lines.copy()
original_lines = lines.copy()  # Keep a copy of the original lines for reference
total_cards = 0

while cards_to_process:
    line = cards_to_process.pop(0)  # Process the next card in the queue
    card_numbers = re.split(r'\||:', line)[1:]
    winning_numbers = set(int(num) for num in card_numbers[0].strip().split())
    drawn_numbers = set(int(num) for num in card_numbers[1].strip().split())
    matches = len(winning_numbers & drawn_numbers)

    total_cards += 1  # Add the current card to the total count

    # Add the corresponding number of subsequent cards to the queue
    card_index = original_lines.index(line)
    for i in range(1, matches + 1):
        if card_index + i < len(original_lines):
            cards_to_process.append(original_lines[card_index + i])

print(total_cards)