import os
import requests
import re
import datetime

aoc_year = 2022
file_day = re.findall('([0-9]{1,2})', __file__.split('/')[-1])[0]
calendar_day = datetime.datetime.now().day

if file_day.isnumeric():
    print(f'''
Assuming file name ({__file__.split("/")[-1]}) ends with puzzle day.
({file_day})
    ''')
    aoc_day = file_day
else:
    # Set day manually.
    print(f'''
Day not found in file name, falling back to date (day of month).
({calendar_day})
    ''')
    aoc_day = calendar_day

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

    f = open(path, 'w')
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


# START #

input_data_test = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''.splitlines()

part_one_answer = 0
part_two_answer = 0

for s in input_data:
    a, b = s.split(',')
    a_rng = a.split('-')
    b_rng = b.split('-')
    a_start = int(a_rng[0])
    a_stop = int(a_rng[1])
    b_start = int(b_rng[0])
    b_stop = int(b_rng[1])

    a_range = range(a_start, a_stop+1)
    b_range = range(b_start, b_stop+1)

    if a_start in list(b_range) and a_stop in list(b_range):
        part_one_answer += 1

    elif b_start in list(a_range) and b_stop in list(a_range):
        part_one_answer += 1

    if (a_start or a_stop) in b_range or (b_start or b_stop) in a_range:
        part_two_answer += 1


print(f'''
    Part 1 : {part_one_answer}  test answer: 2
    Part 2 : {part_two_answer}  test answer: 4
''')
