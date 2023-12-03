import aoc
from pprint import pprint


aoc_year = 2022
aoc_day = 14

__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=Uf_IF_3RbKw
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
input_data = puzzle_data.splitlines()
input_data_test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''.splitlines()
cave_structure = set()
bottom = 0


def refine(data, bottom=bottom):

    for line in data:
        # last = None
        xy_items = [
            list(
                map(int, line_item.split(','))
            ) for line_item in line.strip().split(' -> ')
        ]
        for (x1, y1), (x2, y2) in zip(xy_items, xy_items[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    cave_structure.add(x + y * 1j)  # complex alt.
                    # cave_structure.add((x, y))
                    bottom = max(bottom, y + 1)
    return bottom


def sandfall():
    total = 0
    while True:
        sand = 500  # complex n alt.
        # sand = (500, 0)
        while True:
            # if sand[1] >= bottom:
            if sand.imag >= bottom:
                return total
            if sand + 1j not in cave_structure:  # complex n alt.
                sand += 1j
            # if (sand[0], sand[1] + 1) in cave_structure:
                # sand[1] += 1
                continue
            if sand + 1j - 1 not in cave_structure:
                sand += 1j - 1
            # if (sand[0], sand[1] - 1) not in cave_structure:
                # sand = (sand[0], sand[1] - 1)
                # sand[1][0] -= 1
                continue
            if sand + 1j + 1 not in cave_structure:
                # if (sand[0] + 1, sand[1] + 1) not in cave_structure:
                sand += 1j + 1
                # sand[0] += 1
                continue
            cave_structure.add(sand)
            total += 1
            break


def sandfill():
    total = 0
    while 500 not in cave_structure:
        sand = 500
        while True:
            if sand.imag >= bottom:
                break
            if sand + 1j not in cave_structure:
                sand += 1j
                continue
            if sand + 1j - 1 not in cave_structure:
                sand += 1j - 1
                continue
            if sand + 1j + 1 not in cave_structure:
                sand += 1j + 1
                continue
            break
        cave_structure.add(sand)
        total += 1
    return total


bottom = refine(input_data_test)
part_one_test = sandfall()

cave_structure.clear()
bottom = refine(input_data)
part_one_answer = sandfall()

cave_structure.clear()
bottom = refine(input_data_test)
part_two_test = sandfill()

cave_structure.clear()
bottom = refine(input_data)
part_two_answer = sandfill()

print(f'''
part 1 test:    {part_one_test}
Part 1 answer:  {part_one_answer}
part 1 test:    {part_two_test}
Part 2 answer:  {part_two_answer}
''')

assert part_one_test == 24
assert part_two_test == 93
