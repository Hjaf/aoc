import os
import requests

aoc_year = 2022
aoc_day = '1'
aoc_puzzle_url = f'https://adventofcode.com/{aoc_year}/day/{aoc_day}'
aoc_puzzle_input_url = f'{aoc_puzzle_url}/input'
cwd = os.path.dirname(__file__)
input_file_path = os.path.join(cwd, f'input/day{aoc_day}input.txt')

__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
Puzzle Url   : {aoc_puzzle_url}
Puzzle input : {aoc_puzzle_input_url}
'''


def getAocInput(path):

    f = os.open(path, 'w')
    aoc_headers = {'Cookie': f'session={os.environ.get("AOC_SECRET")}'}
    response = requests.get(f'{aoc_puzzle_input_url}', headers=aoc_headers)
    f.write(response.text)
    f.close()
    return response.text


if os.path.exists(input_file_path):
    input_data = open(input_file_path, 'r', encoding='utf-8').readlines()
else:
    print(
        f'''
No input data file was found for the {aoc_day}/{aoc_year} puzzle.
Attempting to get the input data from {aoc_puzzle_input_url}
Make sure you have set the "AOC_SECRET" environment variable.
        '''
    )
    input_data = getAocInput(input_file_path)


elfcal = {}
elfcal[0] = elf_no = 0

for inp in input_data:
    if inp == '\n':
        elf_no += 1
        elfcal[elf_no] = 0
    else:
        ival = int(inp.strip('\n'))
        elfcal[elf_no] = elfcal[elf_no] + ival

elf_list = list(elfcal.values())
elf_list.sort(reverse=True)

print(f'''
    Part 1 : {elf_list[0]}
    Part 2 : {sum(elf_list[0:3])}
''')
