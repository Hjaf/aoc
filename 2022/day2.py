import os
import requests

aoc_year = 2022
aoc_day = '2'
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


i = 0

A = rock = 1
B = paper = 2
C = scissor = 3

total_points_part_one = total_points_part_two = 0

for r in input_data:

    round = r.strip()
    i += 1

    if round[0] == 'A':  # rock
        point_part_two = paper
        win = paper
        draw = rock
        lose = scissor
    elif round[0] == 'B':  # paper
        point_part_two = scissor
        win = scissor
        draw = paper
        lose = rock
    else:  # scissors
        point_part_two = rock
        win = rock
        draw = scissor
        lose = paper

    if round[2] == 'X':
        point_part_one = rock
        point_part_two = lose
    elif round[2] == 'Y':
        point_part_one = paper
        point_part_two = draw + 3
    else:
        point_part_one = scissor
        point_part_two = win + 6

    if round in {'A X', 'B Y', 'C Z'}:
        point_part_one += 3
    elif round in {'C X', 'A Y', 'B Z'}:
        point_part_one += 6
    elif round in {'B X', 'C Y', 'A Z'}:
        point_part_one += 0
    total_points_part_one += point_part_one
    total_points_part_two += point_part_two

print(f'''
    Part 1 : {total_points_part_one}
    Part 2 : {total_points_part_two}
''')
