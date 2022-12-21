import aoc
import math


aoc_year = 2022
aoc_day = 17

valid_answer_part_one_test = 3068
valid_answer_part_two_test = 1514285714288
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=w9Sk7lvyGZI
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day17p1.py
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day17p2.py
'''
data_input = [
    1 if x == ">" else -1 for x in aoc.fetch_input(aoc_year, aoc_day).strip()
    ]
data_input_test = [
    1 if x == ">" else -1 for x in
    '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'.strip()
]
rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]
seen = {}


def partone(rocks, jets, height=0, rc=0):
    solid = {x - 1j for x in range(7)}
    ri = 0
    rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}

    while rc < 2022:
        for jet in jets:
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rc += 1
                height = max(x.imag for x in solid) + 1
                if rc >= 2022:
                    break
                ri = (ri + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}
            else:
                rock = moved

    return int(height)


def summarize(solid):
    o = [-20] * 7

    for x in solid:
        r = int(x.real)
        i = int(x.imag)
        o[r] = max(o[r], i)
    top = max(o)
    return tuple(x - top for x in o)


def parttwo(jets):
    seen = {}
    T = 1000000000000
    rc = 0
    ri = 0
    solid = {x - 1j for x in range(7)}
    height = 0
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j],
    ]
    rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}

    while rc < T:
        for ji, jet in enumerate(jets):
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rc += 1
                o = height
                height = max(x.imag for x in solid) + 1
                if rc >= T:
                    break
                ri = (ri + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[ri]}
                key = (ji, ri, summarize(solid))
                if key in seen:
                    lrc, lh = seen[key]
                    rem = T - rc
                    rep = rem // (rc - lrc)
                    offset = int(rep * (height - lh))
                    rc += rep * (rc - lrc)
                    seen = {}
                seen[key] = (int(rc), int(height))
            else:
                rock = moved

    return int(height + offset)


answer_part_one_test = partone(rocks, data_input_test)

answer_part_one = partone(rocks, data_input)

answer_part_two_test = parttwo(data_input_test)

answer_part_two = parttwo(data_input)


print(f'''\n
Part one
Test            :    {answer_part_one_test}
Answer:         :    {answer_part_one}

Part two
Test            :    {answer_part_two_test}
Answer          :    {answer_part_two}
''')


# Validation

assert answer_part_one_test == valid_answer_part_one_test, \
    f'(differs from {valid_answer_part_one_test} \
by {abs(valid_answer_part_one_test - answer_part_one_test)})'

assert answer_part_two_test == valid_answer_part_two_test, \
    f'(differs from {valid_answer_part_two_test} \
 by {abs(valid_answer_part_two_test - answer_part_two_test)})'
