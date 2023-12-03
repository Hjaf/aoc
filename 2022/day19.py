import aoc
import re


aoc_year = 2022
aoc_day = 19

valid_answer_part_one_test = 33
valid_answer_part_two_test = 3472
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=H3PSODv4nf0
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day19p1.py
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day19p2.py
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day).splitlines()

data_input = puzzle_data

# The test input looks like it includes newlines,
# which is different from the actual input.

data_input_test = '''Blueprint 1: Each ore robot costs 4 ore. \
Each clay robot costs 2 ore. \
Each obsidian robot costs 3 ore and 14 clay. \
Each geode robot \
costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. \
Each clay robot costs 3 ore. \
Each obsidian robot costs 3 ore and 8 clay. \
Each geode robot costs 3 ore and 12 obsidian.
'''.splitlines()


def dfs(bp, maxspend, cache, time, bots, amt):
    if time == 0:
        return amt[3]

    key = tuple([time, *bots, *amt])
    if key in cache:
        return cache[key]

    maxval = amt[3] + bots[3] * time

    for btype, recipe in enumerate(bp):
        if btype != 3 and bots[btype] >= maxspend[btype]:
            continue

        wait = 0
        for ramt, rtype in recipe:
            if bots[rtype] == 0:
                break
            wait = max(wait, -(-(ramt - amt[rtype]) // bots[rtype]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amt_ = [x + y * (wait + 1) for x, y in zip(amt, bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[btype] += 1
            for i in range(3):
                amt_[i] = min(amt_[i], maxspend[i] * remtime)
            maxval = max(
                maxval,
                dfs(bp, maxspend, cache, remtime, bots_, amt_)
            )

    cache[key] = maxval
    return maxval


def part_one(input):
    total = 0

    for i, line in enumerate(input):
        bp = []
        maxspend = [0, 0, 0]
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            bp.append(recipe)
        v = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        total += (i + 1) * v

    return total


def part_two(input):
    total = 1

    for line in list(input)[:3]:
        bp = []
        maxspend = [0, 0, 0]
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            bp.append(recipe)
        v = dfs(bp, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
        total *= v

    return total


answer_part_one_test = part_one(data_input_test)

answer_part_one = part_one(data_input)

print(f'''\n
Part one
Test            :    {answer_part_one_test}
Answer:         :    {answer_part_one}

Sorry, but part two may take a few minutes.
''')
# Validation

assert answer_part_one_test == valid_answer_part_one_test, \
    f'(differs from {valid_answer_part_one_test} \
by {abs(valid_answer_part_one_test - answer_part_one_test)})'

answer_part_two_test = part_two(data_input_test)
assert answer_part_two_test == valid_answer_part_two_test, \
    f'(differs from {valid_answer_part_two_test} \
by {abs(valid_answer_part_two_test - answer_part_two_test)})'

print(f'''\n
Part two
Test            :    {answer_part_two_test}
''')
answer_part_two = part_two(data_input)
print(f'''
Answer          :    {answer_part_two}
''')
