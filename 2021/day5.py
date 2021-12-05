from os import chdir, path
from collections import Counter
import sys
import numpy
import re
from numpy.core.arrayprint import printoptions

abspath = path.abspath(__file__)
cwd = path.dirname(abspath)
chdir(cwd)

input = open('input/day5input.txt', 'r').readlines()
input_example = open('input/day5inputexample.txt', 'r').readlines()

lines = {}
coords = []
x_coords = []
y_coords = []
x_y_coords = []
option = False
verbose = False

def read_puzzle(data):
    sys.stdout.write('Loading input..\n[ ')
    i = 1
    for row in data:
        if verbose : sys.stdout.write(str(i)+' ')
        line = re.split(r'\s->\s', row.rstrip())
        start = tuple([int(line[0].split(',')[0]), int(line[0].split(',')[1])])
        end = tuple([int(line[1].split(',')[0]), int(line[1].split(',')[1])])
        lines[i] = [
            {'x': start[0], 'y': start[1]},
            {'x': end[0], 'y': end[1]},
            {'raw': row.rstrip()}
        ]
        i += 1
    print(']\nDone.')
    return lines

def output(coords, frequency):
    if verbose :
        print(f'''
all coordinates:
{coords}
coordinate intersection count: 
{frequency}
intersections total: {sum(frequency[1][1:])}
''')
    else:
        print(sum(frequency[1][1:]))

def count_coord_overlap (input_coords):
    
    coordinate_review = list(Counter(input_coords).values())
    (unique, counts) = numpy.unique(coordinate_review, return_counts=True)
    diag_frequency = numpy.asarray((unique, counts))
    return diag_frequency



if sys.argv.__len__()>1:
    option = sys.argv[1].lower()

if option == 'solve':
        print('trying to solve it!')
        lines = read_puzzle(input)
else:
    lines = read_puzzle(input_example)
if option == 'verbose':
    verbose = True

for line in lines:
    vent_lines_x = []
    vent_lines_y = []
    start = lines[line][0]
    end = lines[line][1]
    start_x = start['x']
    start_y = start['y']
    end_x = end['x']
    end_y = end['y']
    delta_x = abs(start_x - end_x)
    delta_y = abs(start_y - end_y)
    start_coordinate = tuple([start_x, start_y])
    if verbose : print(f''' Input: {lines[line][2]['raw']}: ''')
    istep = list(range(0, max(abs(delta_x),abs(delta_y)), 1))
    new_x = start_x
    new_y = start_y
    if(delta_x == 0):
        x_coords.append(start_coordinate)
        x_y_coords.append(start_coordinate)
    if(delta_y == 0): 
        y_coords.append(start_coordinate)
        x_y_coords.append(start_coordinate)
    coords.append(start_coordinate)

    
    for step in istep:
        if verbose : sys.stdout.write(str(step)+ ' ')
        if(start_x > end_x):
            new_x -= 1
        elif (start_x < end_x):
            new_x += 1
        if (start_y > end_y):
            new_y -= 1
        elif (start_y < end_y):
            new_y += 1
        coordinate = tuple([new_x, new_y])
        if(delta_x == 0):
            x_coords.append(coordinate)
            x_y_coords.append(coordinate)
        if(delta_y == 0): 
            y_coords.append(coordinate)
            x_y_coords.append(coordinate)
        
        coords.append(coordinate)

    if verbose : print('] Done.')
    

intersect_frequency = count_coord_overlap(coords)
x_overlap_frequency = count_coord_overlap(x_coords)
y_overlap_frequency = count_coord_overlap(y_coords)
x_y_overlap_frequency = count_coord_overlap(x_y_coords)

if verbose :
    output(x_coords, x_overlap_frequency)
    output(y_coords, y_overlap_frequency)

print('Part One Answer:')
output(x_y_coords, x_y_overlap_frequency)
print('Part Two Answer:')
output(coords, intersect_frequency)