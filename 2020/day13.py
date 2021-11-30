'''
https://adventofcode.com/2020/day/13
(cheated: sources commented in functions)

puzzle_inputs   provided are task examples in same format as the puzzle input.
ans_two         used to verify output.
'''
ans_two = False

puzzle_input = open('input/day13input.txt', 'r').read()
# puzzle_input = '''939
# 7,13,x,x,59,x,31,19''' 
# ans_two = 1068781

# puzzle_input = '''1
# 17,x,13,19'''
# ans_two = 3417

# puzzle_input = '''1
# 67,x,7,59,61'''
# ans_two = 779210

# puzzle_input = '''1
# 67,7,x,59,61'''
# ans_two = 1261476

# puzzle_input = '''1
# 1789,37,47,1889'''
# ans_two = 1202161486

ans_two = False

first_bus = int(puzzle_input.splitlines()[0].strip())
busses = puzzle_input.splitlines()[1].strip().split(',')

i = 0
ib = 0
bus_list = {}
bus_list_two = {}
for bus in busses:
    if bus != 'x':
        if i == 0:
            i = int(bus)
        bus_list[int(bus)] = int(bus)-i 
        bus_list_two[int(bus)] = ib
    i += 1
    ib += 1

def next_bus(i):
    # part one
    first = i
    while True:
        for bus in bus_list.keys():
                if (i % int(bus) == 0):
                    return((i - first) * int(bus))
        i += 1

def ext_euclid(a: int, n: int):
    '''
    Failed to comprehend.
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    a*t ≋ 1 (mod b) 
    This code is stolen from https://github.com/bsounak/Aoc2020/blob/main/day13.py 
    '''
    t = 0
    nt = 1
    r = n
    nr = a
    while nr != 0:
        quot = r // nr
        (t, nt) = (nt, t - quot * nt) 
        (r, nr) = (nr, r - quot * nr) 
        # print(f'q: {quot} t: {t}, nt: {nt}, r: {r}, nr: {nr}')
        '''
        This was unclear to me:
        https://docs.python.org/3.9/reference/simple_stmts.html#augmented-assignment-statements
        'Unlike normal assignments, augmented assignments evaluate the left-hand side before evaluating the right-hand side.
        ...
        With the exception of assigning to tuples and multiple targets in a single statement, the assignment done by augmented assignment statements is handled the same way as normal assignments'
        
        (a, b) = (b, a * b)
        1. a -> b
        2. b -> a * b
        >>> a = 2
        >>> b = 3
        >>> (a, b) = (b, a*b)
        >>> (a, b)
        (3, 6)
        >>> (a, b) = (b, a*b)
        >>> (a, b)
        (6, 18)
        '''
    if r > 1:
        raise Exception("not invertible")
    if t < 0:
        t += n
    return t

def chinese_remainder(a: list, m: list):
    '''
    Failed to comprehend.

    https://www.youtube.com/watch?v=0dbXaSkZ-vc&ab_channel=CenterofMath

    following code is stolen from https://github.com/bsounak/Aoc2020/blob/main/day13.py
    ---
    M = 1
    for v in m:
        M *= v
    Mi = [M // m[i] for i in range(len(m))]
    yi = [inverse(Mi[i], m[i]) for i in range(len(m))]

    X = sum([a[i] * Mi[i] * yi[i] for i in range(len(yi))])
    return X % M
    ---

    https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Computation
    x ≋ a1 -> mod (n1)
    x ≋ a2 -> mod (n2)
    ...
    x ≋ ak -> mod (nk)
    '''
    bigm = 1
    for v in m:
        bigm *= v
    bigm_i = []
    for i in range(len(m)):
        bigm_i.append(bigm // m[i])
    yi = []
    for i in range(len(m)):
        ext_euclid_result = ext_euclid(bigm_i[i], m[i])
        yi.append(ext_euclid_result)
    calcs = []
    for i in range(len(yi)):
        calcs.append(a[i] * bigm_i[i] * yi[i])

    return (sum(calcs) % bigm)



# part one
print(f'part one: {next_bus(first_bus)}')

# part two
offset = list(bus_list.keys())[0]
print(f'part two: {chinese_remainder(list(bus_list.values()), list(bus_list.keys())) + offset}')
# part two example verification
if ans_two and ans_two == (chinese_remainder(list(bus_list.values()), list(bus_list.keys())) + offset):
    print(f'Answer correct ({ans_two})')


'''
https://github.com/mdjaere/adventofcode2020/tree/main/13/python

import fileinput
notes = [note.strip() for note in fileinput.input()]
time = int(notes[0])
busses = [{"id": int(route), "offset": int(offset)}
          for offset, route in enumerate(notes[1].split(",")) if route != "x"]
# Part 1
first_bus = sorted([[bus["id"], bus["id"] - time % bus["id"]]
                    for bus in busses], key=lambda x: x[1])[0]
print("Part 1:", first_bus[0] * first_bus[1])
# Part 2
time = 1
jump = 1
for bus in busses:
    while not (time + bus["offset"]) % bus["id"] == 0:
        time += jump
    jump *= bus["id"]
print("Part 2:", time)
'''

time = 1
jump = 1
i = 0
for bus in busses:
    if bus != 'x':
        b = int(bus)
        while not (time + i) % b == 0:
            time += jump
        jump *= b
    i += 1
print(f'part two: {time} (solution by mdjaere)')
