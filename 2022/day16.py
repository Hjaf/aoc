import aoc
import re
from collections import deque


aoc_year = 2022
aoc_day = 16

valid_answer_part_one_test = 1651
valid_answer_part_two_test = 1707
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=bLMj50cpOug
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day16p1.py
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day16p2.py
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)

data_input = puzzle_data.splitlines()
data_input_test = \
    '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''.splitlines()
valves = {}
tunnels = {}
rates = []

max_possible_score = 0
minutes_available = 30

dists = {}
not_empty = []
indices = {}
cache = {}


def parse_input(data_input):

    valves.clear()
    tunnels.clear()
    rates.clear()
    indices.clear()
    cache.clear()
    not_empty.clear()

    for line in data_input:
        line_arr = line.split(' ')
        valve, rate, downstream = [
            line_arr[1],
            int((line_arr[4].split('=')[1])[:-1]),
            [ds.strip(',') for ds in list(line_arr[9:])]
        ]
        if rate > 0:
            rates.append(rate)
        if valve not in valves.keys():
            valves[valve] = rate
            tunnels[valve] = downstream


def max_val(tm, rates):
    max_val = 0
    i = 0
    for v in sorted(rates, reverse=True):
        max_val += v * max((tm - i), 0)
        i += 1
    return max_val


def defi_search(time, valve, bmask):

    if (time, valve, bmask) in cache:
        return cache[(time, valve, bmask)]

    m_val = 0
    for n in dists[valve]:
        bit = 1 << indices[n]
        if bmask & bit:
            '''
       mask 01010100
    A & bit      100
    B & bit     1100
            --------
    A bit   00000100 == true
            -----^--
    B bit   00000000 == false
            ----^---
            '''
            continue
        rtime = time - dists[valve][n] - 1
        if rtime <= 0:
            continue
        m_val = max(
            m_val,
            defi_search(rtime, n, bmask | bit) + valves[n] * rtime
            )
    cache[(time, valve, bmask)] = m_val
    return m_val


def prep():

    for valve in valves:

        if valve != 'AA' and not valves[valve]:
            continue

        if valve != 'AA':
            not_empty.append(valve)

        dists[valve] = {valve: 0, 'AA': 0}
        checked = {valve}

        q = deque([(0, valve)])

        while q:
            dist, pos = q.popleft()
            for n in tunnels[pos]:
                if n in checked:
                    continue
                checked.add(n)
                if valves[n]:  # ignore empty
                    dists[valve][n] = dist + 1
                q.append((dist + 1, n))

        del dists[valve][valve]

        if valve != 'AA':
            del dists[valve]['AA']

    for index, element in enumerate(not_empty):
        indices[element] = index


def valve_opener(input):
    parse_input(input)
    prep()
    return defi_search(30, 'AA', 0)


def valve_helper(input):
    parse_input(input)
    prep()
    elefant_bit = (1 << len(not_empty)) - 1

    ans = 0
    for i in range((elefant_bit + 1) // 2):
        ans = max(
            ans,
            defi_search(
                26,
                'AA',
                i
            ) + defi_search(
                26,
                'AA',
                elefant_bit ^ i
            )
        )
    return ans


print('Solving puzzles: ', end='')
answer_part_one_test = valve_opener(data_input_test)
print('1', end='')
answer_part_one = valve_opener(data_input)
print(', 2', end='')
answer_part_two_test = valve_helper(data_input_test)
print(', 3', end='')
answer_part_two = valve_helper(data_input)
print(', 4 done. ')

print(f'''
Part one
Test            :    {answer_part_one_test}
Answer:         :    {answer_part_one}

Part two
Test            :    {answer_part_two_test}
Answer          :    {answer_part_two}
''')

# Validation

assert answer_part_one_test == valid_answer_part_one_test
assert answer_part_two_test == valid_answer_part_two_test
assert answer_part_one not in [0]
assert answer_part_two not in [0]
