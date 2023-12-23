import aoc
import re


aoc_year = 2023
aoc_day = 3

valid_answer_part_one_example = 4361
valid_answer_part_two_example = 467835
answer_part_one_example = 0
answer_part_two_example = 0

answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
puzzle_data_example_one = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

puzzle_data_example_two = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

### SOLUTION #### 

def part_one(input):
    lines = input.splitlines()
    numbers = []
    proxy_map = {}
    found = set()
        
    for line_no, line in enumerate(lines):
        for number in re.finditer(r'\d+', line):
            number_index = len(numbers)
            numbers.append(int(number.group()))
            for x_span in range(number.start(), number.end()):
                proxy_map[line_no,x_span] = number_index

    # print(proxy_map)

    for line_no, line in enumerate(lines):
        for symbol in re.finditer(r'[^\.\d]', line):
            for y_span in range(line_no-1, line_no+2):
                for x_span in range(symbol.start()-1, symbol.start()+2):
                    if proxy_map.get((y_span,x_span)) != None:
                        found.add(proxy_map[y_span,x_span])


    return(sum([numbers[i] for i in found]))


def part_two(input):
    lines = input.splitlines()
    ratio = 0
    numbers = []
    proxy_map = {}
    
    for line_no, line in enumerate(lines):
        for number in re.finditer(r'\d+', line):
            number_index = len(numbers)
            numbers.append(int(number.group()))
            for x_span in range(number.start(), number.end()):
                proxy_map[line_no,x_span] = number_index
        

    for line_no, line in enumerate(lines):
        for symbol in re.finditer(r'[^\.\d]', line):
            found = set()
            for y_span in range(line_no-1, line_no+2):
                for x_span in range(symbol.start()-1, symbol.start()+2):
                    if proxy_map.get((y_span,x_span)) != None:
                        found.add(proxy_map[y_span,x_span])
            if len(found) == 2:
                ratio += numbers[found.pop()] * numbers[found.pop()]

    return ratio

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
Answer          :    {answer_part_two}
answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
