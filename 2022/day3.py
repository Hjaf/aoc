import os
import requests
import re

aoc_year = 2022
aoc_day = '3'
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
    # if len(os.environ.get("AOC_SECRET")) < 1:
    #     os.environ["AOC_SECRET"] = "${{ secrets.AOC_SECRET}}"
    f = open(path, 'w')
    aoc_headers = {'Cookie': f'session={"${{ secrets.AOC_SECRET}}"}'}
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

input_data_test = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''.splitlines()

item_types = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
rearrange_priorites = dict(zip(item_types, range(1, 53)))

part_one_answer = 0
part_two_answer = 0
group_size = 3
e = 0
group_number = 1
group_item_types = set()

# for rx in input_data_test:
for rx in input_data:
    r = rx.strip()
    item_size = int(r.__len__() / 2)
    first_item = r[:(item_size)]
    second_item = r[(item_size):]
    in_both = re.findall(f'[{first_item}]', second_item)

    duplicates = list(dict.fromkeys(in_both))

    dpoints = 0
    for d in duplicates:
        dpoints += rearrange_priorites[d]
    part_one_answer += dpoints

    # part two

    if (group_size <= e or e == 0):
        group_item_types = set(list(dict.fromkeys(r)))
        group_number += 1  # next group
        e = 1   # first elf in group
    else:
        e += 1  # next elf in group
        group_item_types.intersection_update(set(list(dict.fromkeys(r))))

    epoints = 0
    if (group_size == e):
        for t in group_item_types:
            epoints += rearrange_priorites[t]
    part_two_answer += epoints

    # part two end

print(f'''

    Part 1 : {part_one_answer}      (Part 1 test output: 157)
    Part 2 : {part_two_answer}      (Part 2 test output: 70)

''')