import requests
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


def fetch_input(aoc_year=year, aoc_day=day, codespace=False):
    '''
    Returns the puzzle input contents as a raw string, if the file is not
    found locally it fetches the latest puzzle from advent of code.

    Args:
        aoc_year: year (defaults to current year) (int)
        aoc_day: day (defaults to current day of month) (int)
        codespace: if the environment is a codespace (boolean)

    Returns:
        Puzzle input (string)
    '''
    aoc_puzzle_url = f'https://adventofcode.com/{aoc_year}/day/{aoc_day}'
    aoc_puzzle_input_url = f'{aoc_puzzle_url}/input'
    cwd = os.path.dirname(__file__)
    aoc_input_folder = os.path.join(cwd, 'input')
    input_file_path = os.path.join(cwd, f'input/day{aoc_day}input.txt')
    if not os.path.exists(aoc_input_folder):
        os.mkdir(aoc_input_folder)
        print(f'Created puzzle input folder ({aoc_input_folder})')
    if os.path.exists(input_file_path):
        return open(input_file_path, 'r', encoding='utf-8').read()
    else:
        print(
            f'''
No input data file was found for the {aoc_day}/{aoc_year} puzzle.
Attempting to get the input data from {aoc_puzzle_input_url}
            '''
        )
        if codespace and os.environ.get("AOC_SECRET") is None:
            print('Environment variable not set, setting from github-secrets')
            os.environ["AOC_SECRET"] = "${{ secrets.AOC_SECRET }}"
        elif not codespace and os.environ.get("AOC_SECRET") is None:
            # if still none.
            print('''
Not able to set the session secret required for getting
the puzzle input! Make sure the environment variable
'AOC_SECRET' is defined (securely) in this environment
or github secret and try again.
`export AOC_SECRET="XXXXX"`
The secret is the value of the session cookie for adventofcode.com
            ''')
            return '-'
        else:
            f = open(input_file_path, 'w')
            aoc_headers = \
                {'Cookie': f'session={os.environ.get("AOC_SECRET")}'}
            response = requests.get(
                f'{aoc_puzzle_input_url}', headers=aoc_headers
            )
            f.write(response.text)
            f.close()
            return response.text
