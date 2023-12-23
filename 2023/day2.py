import aoc
import re


aoc_year = 2023
aoc_day = 2

valid_answer_part_one_example = 8
valid_answer_part_two_example = 0
answer_part_one_example = 0
answer_part_two_example = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)

# The test input looks like it includes newlines,
# which is different from the actual input.

puzzle_data_example_one = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.strip()

puzzle_data_example_two = puzzle_data_example_one 

def read_game(input):
    game_id = input.strip().split(':')[0].split(': ')[-1].strip()
    game_hands = []
    for pick in input.split(';'):
        print(pick)

read_game(puzzle_data_example_one)

def part_one_fup(inp):
    valid_games = []
    red_max = 12
    green_max = 13
    blue_max = 14
    for game in inp.splitlines():
        g = game.split(':')
        game_id = int(g[0][4:])
        valid = False
        for grab in g[1].split(';'):
            # print(grab)
            green_count = 0
            red_count = 0
            blue_count = 0
            for dices in grab.split(','):
                d = dices.strip().split(' ')
                match d[1]:
                    case 'blue':
                        blue_count = int(d[0])
                    case 'red':
                        red_count = int(d[0])
                    case 'green':
                        green_count = int(d[0])

            if green_count <= green_max and red_count <= red_max and blue_count <= blue_max:
                valid = True
                # break
            # else:
            #     print(f'''
            #     {game} - *INVALID*
            #     game ID: {game_id}
            #         green_count: {green_count}
            #         red_count: {red_count}
            #         blue_count: {blue_count}
            #     ''')
        if valid:
            valid_games.append(game_id)
    print(valid_games)
        
    return 8 #sum(valid_games)+

def part_one(input):
    lines = input.splitlines()
    games = [" ".join(line.strip().split(" ")[2:]).split(";") for line in lines]
    games = [[r.strip().split(", ") for r in g] for g in games]
    ans_1 = []
    limit = {"red":12,"green":13,"blue":14}
    ans_2= []
    for i, game in enumerate(games):
        above_limit = False
        max_count = {"red":0,"green":0,"blue":0}
        for samples in game:
            count = {"red":0,"green":0,"blue":0}
            for entry in samples:
                val, key = entry.split(" ")
            count[key] = int(val)
            for k,v in count.items():
                if v > limit[k]:
                    above_limit = True
                max_count[k]=max(max_count[k],v)
        if not above_limit:
            ans_1.append(i+1)
        g_power = 1
        for v in max_count.values():
            g_power *= v
        ans_2.append(g_power)
    return sum(ans_1)

def part_two(input):
    lines = input.splitlines()
    games = [" ".join(line.strip().split(" ")[2:]).split(";") for line in lines]
    games = [[r.strip().split(", ") for r in g] for g in games]
    ans_1 = []
    limit = {"red":12,"green":13,"blue":14}
    ans_2= []
    for i, game in enumerate(games):
        above_limit = False
        max_count = {"red":0,"green":0,"blue":0}
        for samples in game:
            count = {"red":0,"green":0,"blue":0}
            for entry in samples:
                val, key = entry.split(" ")
            count[key] = int(val)
            for k,v in count.items():
                if v > limit[k]:
                    above_limit = True
                max_count[k]=max(max_count[k],v)
        if not above_limit:
            ans_1.append(i+1)
        g_power = 1
        for v in max_count.values():
            g_power *= v
        ans_2.append(g_power)
    return sum(ans_2)


answer_part_one_example = part_one(puzzle_data_example_one)


# Validation

assert answer_part_one_example == valid_answer_part_one_example, \
    f'(differs from {valid_answer_part_one_example} \
by {abs(valid_answer_part_one_example - answer_part_one_example)})'



answer_part_one = part_one(puzzle_data)
#### OUTPUT ###

# Part One

print(f'''\n
Part one
Test            :    {answer_part_one_example}
Answer:         :    {answer_part_one}
''')

# Part Two
# answer_part_two_example = part_two(puzzle_data_example_two)
# assert answer_part_two_example == valid_answer_part_two_example, \
#     f'(differs from {valid_answer_part_two_example} \
# by {abs(valid_answer_part_two_example - answer_part_two_example)})'

answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
