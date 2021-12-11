# day 11 dumboflash
from numpy import *
input_file = open('../input/day11input.txt', 'r').readlines()
# input_file = open('../input/day11inputexample.txt', 'r').readlines()
input = []
input_file = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.splitlines()

for row in input_file:
    input.append(list(row.strip()))
grid = array(input)


def adjacent(coords, range=1):
    x, y = coords
    # print(f'X:{x} Y:{y}')
    adj_array = array([
        [(x-1, y-1), (x, y-1),(x+1, y-1)],
        [(x-1, y), (x, y), (x+1, y)], 
        [(x-1, y+1), (x, y+1), (x+1, y+1)]
    ])
    for r in adj_array:
        print()
    # for c in adj_array:
    #     gri
    
    # return adj_array

# def flash(coordinates, )

grid_width = len(grid[0])
for ri, row in enumerate(grid):
      if ri > 0:
          for ci, column in enumerate(row):
              if ci > 0 and ci < grid_width:
                coordinate =  (ci, ri)
                # adjacent(coordinate)
                # print('test')
                adjacent(coordinate)


# def ripple(coords, pos):

# print(test[1][1])
