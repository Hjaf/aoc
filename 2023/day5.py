import aoc
import re
import pprint


aoc_year = 2023
aoc_day = 5

valid_answer_part_one_example = 35
valid_answer_part_two_example = 30
answer_part_one_example = 0
answer_part_two_example = 0

answer_part_one = 0
answer_part_two = 0


__doc__ = f'''
Advent of code: day {aoc_day} {aoc_year}
'''

puzzle_data = aoc.fetch_input(aoc_year, aoc_day)
puzzle_data_example_one = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

puzzle_data_example_two = str(puzzle_data_example_one)

### SOLUTION #### 

seeds = []
mappings = {}

def load_data(input):
    seeds_string = input.split('seeds: ')[1].splitlines()[0].split(' ')
    for seed in seeds_string:
        seeds.append(int(seed))
    
    soil_map = input.split('seed-to-soil map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['soil'] = [[int(sm.strip()) for sm in sml.split(' ')] for sml in soil_map]

    fertilizer_map = input.split('soil-to-fertilizer map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['fertilizer'] = [[int(fm.strip()) for fm in fml.split(' ')] for fml in fertilizer_map] 

    water_map = input.split('water-to-light map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['light'] = [[int(wm.strip()) for wm in wml.split(' ')] for wml in water_map]

    temperature_map = input.split('light-to-temperature map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['temperature'] = [[int(tm.strip()) for tm in tml.split(' ')] for tml in temperature_map]
    
    humidity_map = input.split('temperature-to-humidity map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['humidity'] = [[int(hm.strip()) for hm in hml.split(' ')] for hml in humidity_map]

    location_map = input.split('humidity-to-location map:')[1].split('\n\n')[0].strip().splitlines()
    mappings['location'] = [[int(lm.strip()) for lm in lml.split(' ')] for lml in location_map]

    print(mappings)
#     print(f'''
# seeds: {seeds}

# soil: {soil_map}

# fertilizer: {fertilizer_map}

# water 2 light: {water_to_light}

# light 2 temp : {light_to_temp}

# temp 2 humid: {temp_to_humidity}

# humid 2 location : {humidity_to_location}
#     ''')
    # 1. destination range start
    # 2. source range start 
    # 3. range length


def part_one(input):
    load_data(input)
    
    return len(input)


def part_two(input): 
    lines = input.splitlines()

    return len(input)

    
answer_part_one = part_one(puzzle_data)    

#### OUTPUT ####

# Part One
# Test
answer_part_one_example = part_one(puzzle_data_example_one)
assert answer_part_one_example == valid_answer_part_one_example, \
    f'(differs from {valid_answer_part_one_example} \
by {abs(valid_answer_part_one_example - answer_part_one_example)})'

# Solve
answer_part_one = part_one(puzzle_data)
print(f'''\n
Part one
Test            :    {answer_part_one_example}
Answer:         :    {answer_part_one}
''')
# wrong submissions: 43707

# Part Two

# Test
answer_part_two_example = part_two(puzzle_data_example_two)
assert answer_part_two_example == valid_answer_part_two_example, \
    f'(differs from {valid_answer_part_two_example} \
by {abs(valid_answer_part_two_example - answer_part_two_example)})'

# Solve
Answer          :    {answer_part_two}
answer_part_two = part_two(puzzle_data)

print(f'''\n
Part two
Test            :    {answer_part_two_example}
Answer          :    {answer_part_two}
''')
