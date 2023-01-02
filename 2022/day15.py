import aoc
import re
from pprint import pprint


aoc_year = 2022
aoc_day = 15

__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=OG1QwJ2RKsU
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
input_data = puzzle_data.splitlines()
input_data_test = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''.splitlines()

pattern = re.compile(r'-?\d+')


def part_one(raw_data, Y=10):
    no_beacon = set()
    known_beacons = set()
    for line in raw_data:
        sx, sy, bx, by = map(int, pattern.findall(line))

        distance = abs(sx - bx) + abs(sy - by)
        offset = distance - abs(sy - Y)

        if offset < 0:
            continue

        low_x = sx - offset
        high_x = sx + offset

        for x in range(low_x, high_x + 1):
            no_beacon.add(x)

        if by == Y:
            known_beacons.add(bx)

    return len(no_beacon - known_beacons)


def part_two(raw_data, M):
    multiplier = max(4_000_000, M)
    lines = [list(map(int, pattern.findall(line))) for line in raw_data]
    for Y in range(M + 1):
        if Y % 10000 == 0 and Y > 1:
            print(f'Row (y): {Y} of {M} rows (max)\r', end='')
        intervals = []
        for sx, sy, bx, by in lines:

            distance = abs(sx - bx) + abs(sy - by)
            offset = distance - abs(sy - Y)

            if offset < 0:
                continue

            low_x = sx - offset
            high_x = sx + offset

            intervals.append((low_x, high_x))

        intervals.sort()

        q = []

        for lo, hi in intervals:
            if not q:
                q.append([lo, hi])
                continue

            _, qhi = q[-1]

            if lo > qhi + 1:
                q.append([lo, hi])
                continue

            q[-1][1] = max(qhi, hi)

        x = 0
        for lo, hi in q:
            if x < lo:
                ans = (x * multiplier) + Y
                print(f'x={x}, y={Y} not covered. Score/answer: {ans}') \
                    if ans > 4_000_000 else None
            x = max(x, hi + 1)
            if x > M:
                break
    return ans


answer_part_one_test = part_one(input_data_test, 10)
answer_part_one = part_one(input_data, 2_000_000)

answer_part_two_test = part_two(input_data_test, 20)
answer_part_two = part_two(input_data, 4_000_000)


print(f'''\n
Part one 
Test            :    {answer_part_one_test} (26)
Answer:         :    {answer_part_one}

Part two
Test            :    {answer_part_two_test} (56000011)
Answer          :    {answer_part_two}
''')

assert answer_part_one_test == 26
assert answer_part_two_test == 56000011
assert answer_part_one not in [0]
assert answer_part_two not in [0]
