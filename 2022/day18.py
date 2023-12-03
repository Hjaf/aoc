import aoc
from collections import deque


aoc_year = 2022
aoc_day = 18

valid_answer_part_one_test = 64
valid_answer_part_two_test = 58
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

https://www.youtube.com/watch?v=7tlWvZTPz1c
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day18p1.py
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day18p2.py
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)

data_input = puzzle_data.splitlines()
data_input_test = \
    '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''.splitlines()

droplet = set()
free = set()
faces = {}


def part_one(input):
    faces.clear()
    offsets = [
        (0, 0, 0.5),
        (0, 0.5, 0),
        (0.5, 0, 0),
        (0, 0, -0.5),
        (0, -0.5, 0),
        (-0.5, 0, 0)
    ]

    for line in input:
        x, y, z = map(int, line.split(","))

        for dx, dy, dz in offsets:
            k = (x + dx, y + dy, z + dz)
            if k not in faces:
                faces[k] = 0
            faces[k] += 1

    return list(faces.values()).count(1)


def part_two(input):
    faces.clear()
    droplet.clear()
    offsets = [
        (0, 0, 0.5),
        (0, 0.5, 0),
        (0.5, 0, 0),
        (0, 0, -0.5),
        (0, -0.5, 0),
        (-0.5, 0, 0)
    ]
    mx = my = mz = float("inf")
    Mx = My = Mz = -float("inf")

    for line in input:
        x, y, z = cell = tuple(map(int, line.split(",")))
        droplet.add(cell)
        mx = min(mx, x)
        my = min(my, y)
        mz = min(mz, z)
        Mx = max(Mx, x)
        My = max(My, y)
        Mz = max(Mz, z)

        for dx, dy, dz in offsets:
            k = (x + dx, y + dy, z + dz)
            if k not in faces:
                faces[k] = 0
            faces[k] += 1

    mx -= 1
    my -= 1
    mz -= 1

    Mx += 1
    My += 1
    Mz += 1

    q = deque([(mx, my, mz)])
    air = {(mx, my, mz)}

    while q:
        x, y, z = q.popleft()

        for dx, dy, dz in offsets:
            nx, ny, nz = k = (x + dx * 2, y + dy * 2, z + dz * 2)
            if not (mx <= nx <= Mx and my <= ny <= My and mz <= nz <= Mz):
                continue
            if k in droplet or k in air:
                continue
            air.add(k)
            q.append(k)

    free.clear()

    for x, y, z in air:
        for dx, dy, dz in offsets:
            free.add((x + dx, y + dy, z + dz))

    return len(set(faces) & free)


answer_part_one_test = part_one(data_input_test)

answer_part_one = part_one(data_input)

answer_part_two_test = part_two(data_input_test)

answer_part_two = part_two(data_input)

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
