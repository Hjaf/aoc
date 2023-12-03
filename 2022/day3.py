import re
import aoc


aoc_year = 2022
aoc_day = 2

valid_answer_part_one_test = 157
valid_answer_part_two_test = 70
answer_part_one_test = 0
answer_part_two_test = 0


answer_part_one = 0
answer_part_two = 0

input_data = aoc.fetch_input(aoc_year, aoc_day).splitlines()

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
            # if t != ' ':
            epoints += rearrange_priorites[t]
            # else: 
            #     print(t)
    part_two_answer += epoints

    # part two end

print(f'''

    Part 1 : {part_one_answer}      (Part 1 test output: 157)
    Part 2 : {part_two_answer}      (Part 2 test output: 70)

''')
