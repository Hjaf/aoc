import aoc

aoc_year = 2022
aoc_day = 13

valid_answer_part_one_test = 13
valid_answer_part_two_test = 140
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}

Helped by:

https://www.youtube.com/watch?v=k6WOnlpiYBQ
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day13p1.py
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day13p2.py
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
input_data_raw = puzzle_data.strip()
input_data = list(map(str.splitlines, input_data_raw.split('\n\n')))

input_data_test_raw = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''.strip()

input_data_test = list(map(str.splitlines, input_data_test_raw.split('\n\n')))


def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b in zip(x, y):
        res = compare(a, b)
        if res:
            return res

    return len(x) - len(y)


def part_one(input):
    ans = 0
    for i, (first, last) in enumerate(input):
        if compare(eval(first), eval(last)) < 0:
            ans += i + 1
    return ans


def part_two(input):
    input = list(map(eval, input.split()))
    a = 1   # two
    b = 2   # six
    for i in input:
        if compare(i, [[2]]) < 0:
            a += 1
            b += 1
        elif compare(i, [[6]]) < 0:
            b += 1
    return b * a


answer_part_one_test = part_one(input_data_test)
answer_part_one = part_one(input_data)

answer_part_two_test = part_two(input_data_test_raw)
answer_part_two = part_two(input_data_raw)

print(f'''\n
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
