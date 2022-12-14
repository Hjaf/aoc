import requests
from copy import deepcopy
import datetime
import os

cwd = os.path.dirname(__file__)
day = datetime.datetime.today().day
year = datetime.datetime.today().year

__doc__ = f'''
Will attempt getting the puzzle input from advent of code.

Note:
requires aoc_session value defined as github secret named "AOC_SECRET"
'''


def fetch_input(aoc_year=year, aoc_day=day):
    '''
    Returns the puzzle input contents, if the file is not found it
    fetches the latest puzzle from advent of code.

    Args:
        aoc_year: year (defaults to current year) (int)
        aoc_day: day (defaults to current day of month) (int)

    Returns:
        Puzzle input (string)
    '''
    aoc_puzzle_url = f'https://adventofcode.com/{aoc_year}/day/{aoc_day}'
    aoc_puzzle_input_url = f'{aoc_puzzle_url}/input'
    cwd = os.path.dirname(__file__)
    input_file_path = os.path.join(cwd, f'input/day{aoc_day}input.txt')
    if os.path.exists(input_file_path):
        return open(input_file_path, 'r', encoding='utf-8').read()
    else:
        print(
            f'''
    No input data file was found for the {aoc_day}/{aoc_year} puzzle.
    Attempting to get the input data from {aoc_puzzle_input_url}
    Make sure you have set the "AOC_SECRET" environment variable.
            '''
        )
        if os.environ.get("AOC_SECRET") is None:
            print('environment missing, setting from github-secrets')
            os.environ["AOC_SECRET"] = "${{ secrets.AOC_SECRET}}"
        f = open(input_file_path, 'w')
        aoc_headers = {'Cookie': f'session={os.environ.get("AOC_SECRET")}'}
        response = requests.get(f'{aoc_puzzle_input_url}', headers=aoc_headers)
        f.write(response.text)
        f.close()
        return response.text
