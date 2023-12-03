import aoc
import re


aoc_year = 2023
aoc_day = 2

valid_answer_part_one_example = 8
valid_answer_part_two_example = 0
answer_part_one_example = 0
answer_part_two_example = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)

# The test input looks like it includes newlines,
# which is different from the actual input.

puzzle_data_example_one = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.strip()

puzzle_data_example_two = puzzle_data_example_one 

def part_one(input):
    return input

def part_two(input):
    return input


answer_part_one_example = part_one(puzzle_data_example_one)

answer_part_two_example = part_two(puzzle_data_example_two)

# Validation

assert answer_part_one_example == valid_answer_part_one_example, \
    f'(differs from {valid_answer_part_one_example} \
by {abs(valid_answer_part_one_example - answer_part_one_example)})'


answer_part_two_example = part_two(puzzle_data_example_two)
assert answer_part_two_example == valid_answer_part_two_example, \
    f'(differs from {valid_answer_part_two_example} \
by {abs(valid_answer_part_two_example - answer_part_two_example)})'


answer_part_one = part_one(puzzle_data)
#### OUTPUT ###

# Part One

print(f'''\n
Part one
Test            :    {answer_part_one_example}
Answer:         :    {answer_part_one}
''')

# Part Two
answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
