import aoc
import re
import pprint


aoc_year = 2023
aoc_day = 4

valid_answer_part_one_example = 13
valid_answer_part_two_example = 30
answer_part_one_example = 0
answer_part_two_example = 0

answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
puzzle_data_example_one = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

puzzle_data_example_two = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

### SOLUTION #### 
def read_card(card):
    id = card.split(':')[0].split(' ')[1]
    numbers = list(filter(None, card.split('|')[-1].strip().split(' ')))
    winning_numbers = list(filter(None, card.split(':')[1].strip().split('|')[0].strip().split(' ')))
    return id, winning_numbers, numbers

def part_one(input):
    cards = input.splitlines()
    total_points = 0
    for card in cards:
        card_points = 0
        id, winning_numbers, numbers = read_card(card)
        for winning_number in winning_numbers:
            if winning_number.strip() in numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points * 2
        total_points += card_points
    return total_points

def check_card(winning_numbers, numbers):
    card_score = 0
    for winning_number in winning_numbers:
        if winning_number in numbers:
            card_score += 1
    return card_score

def part_two(input): 
    lines = input.splitlines()
    winners = []
    polled = []
    for line in lines:
        win_raw, poll_raw = line.split(": ")[1].split("|")
        winners.append(set(int(x) for x in win_raw.strip().split(" ") if x))
        polled.append(set(int(x) for x in poll_raw.strip().split(" ") if x))
    scores_1 = []
    n_matches = []
    for win, poll in zip(winners, polled):
        n_matching = len(set.intersection(win, poll))
        n_matches.append(n_matching)
        score = n_matching if n_matching <= 2 else pow(2, n_matching - 1)
        scores_1.append(score)

    counts = [1] * len(lines)
    for i, n_match in enumerate(n_matches):
        for j in range(n_match):
            next_card = i+j+1
            if next_card >= len(counts):
                continue
            counts[next_card] += counts[i]

    return sum(counts)

    
    

#### OUTPUT ####

# Part One
# Test
answer_part_one_example = part_one(puzzle_data_example_one)
assert answer_part_one_example == valid_answer_part_one_example, \
    f'(differs from {valid_answer_part_one_example} \
by {abs(valid_answer_part_one_example - answer_part_one_example)})'

# Solve
answer_part_one = part_one(puzzle_data)
print(f'''\n
Part one
Test            :    {answer_part_one_example}
Answer:         :    {answer_part_one}
''')
# wrong submissions: 43707

# Part Two

# Test
answer_part_two_example = part_two(puzzle_data_example_two)
assert answer_part_two_example == valid_answer_part_two_example, \
    f'(differs from {valid_answer_part_two_example} \
by {abs(valid_answer_part_two_example - answer_part_two_example)})'

# Solve
Answer          :    {answer_part_two}
answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
