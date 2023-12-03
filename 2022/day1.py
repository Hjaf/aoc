import aoc

aoc_year = 2022
aoc_day = 1

__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
input_data = puzzle_data.splitlines()

input_data_test = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''.splitlines()

elfcal = {}
elfcal[0] = elf_no = 0

for inp in input_data:
    if inp == '':
        elf_no += 1
        elfcal[elf_no] = 0
    else:
        ival = int(inp)
        elfcal[elf_no] = elfcal[elf_no] + ival

elf_list = list(elfcal.values())
elf_list.sort(reverse=True)

print(f'''
    Part 1 : {elf_list[0]}
    Part 2 : {sum(elf_list[0:3])}
''')
