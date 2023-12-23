import aoc
import re
import pprint


aoc_year = 2023
aoc_day = 7

valid_answer_part_one_example = 6440
valid_answer_part_two_example = 6440
answer_part_one_example = 0
answer_part_two_example = 0

answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
puzzle_data_example_one = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

puzzle_data_example_two = str(puzzle_data_example_one)

### SOLUTION #### 

seeds = []
mappings = {}

def load_data(input):
    return input

def part_one(input):
    load_data(input)
    
    return len(input)


def part_two(input): 
    lines = input.splitlines()

    return len(input)

    
answer_part_one = part_one(puzzle_data)    

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
