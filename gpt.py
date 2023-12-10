import re

# Sample input data
lines = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

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
