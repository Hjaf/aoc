import os
import requests
import re

aoc_year = 2022
aoc_day = '11'
aoc_puzzle_url = f'https://adventofcode.com/{aoc_year}/day/{aoc_day}'
aoc_puzzle_input_url = f'{aoc_puzzle_url}/input'
cwd = os.path.dirname(__file__)
input_file_path = os.path.join(cwd, f'input/day{aoc_day}input.txt')

__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
Puzzle Url   : {aoc_puzzle_url}
Puzzle input : {aoc_puzzle_input_url}

Note:
Will attempt getting the puzzle input from advent of code. 
requires aoc_session value defined as github secret named "AOC_SECRET"
'''


def getAocInput(path):
    if os.environ.get("AOC_SECRET") is None:
        print('environment missing, setting from github-secrets')
        os.environ["AOC_SECRET"] = "${{ secrets.AOC_SECRET}}"
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

