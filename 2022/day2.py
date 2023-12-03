import re
import aoc


aoc_year = 2022
aoc_day = 2

valid_answer_part_one_test = 15
valid_answer_part_two_test = 12
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0

input_data = aoc.fetch_input(aoc_year, aoc_day).splitlines()

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
