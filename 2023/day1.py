import aoc
import re


aoc_year = 2023
aoc_day = 1

valid_answer_part_one_example = 142
valid_answer_part_two_example = 281
answer_part_one_example = 0
answer_part_two_example = 0

answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)

puzzle_data_example_one = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

puzzle_data_example_two = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

### SOLUTION #### 

def part_one(inp):
    input_arr = inp.splitlines()
    total = 0
    for inp in input_arr:
        numbers = re.sub("[^0-9]","", inp)
        if len(numbers) > 0 :
            first_last =(f'''{numbers[0]}{numbers[-1]}''')
            total += int(first_last) 
            
    return total

# part two

def part_two(inp):
    num_embed = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for k, v in num_embed.items():
        inp = inp.replace(k, v)
    return part_one(inp)

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

# Part Two

# Test
answer_part_two_example = part_two(puzzle_data_example_two)
assert answer_part_two_example == valid_answer_part_two_example, \
    f'(differs from {valid_answer_part_two_example} \
by {abs(valid_answer_part_two_example - answer_part_two_example)})'

# Solve
answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
