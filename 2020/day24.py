tilewalks = open('input/day24input.txt', 'r').readlines()

##
# Grid layout chosen for plot experiments.
# hexagonal grid 4 by 3, 
# center x distance is 4 
# center y distance is 3
# center diagonal distance is 5 
# (2(x) + 3(y)) 
##

step_no = 0
walk_no = 0
path = {}
tiles = {}
directions = {'e': [4,0], 'se': [2,-3], 'sw': [-2,-3], 'w': [-4,0], 'nw': [-2,3],'ne': [2,3]}
coordinate = '0;0'
path[coordinate] = {walk_no, step_no, ''}
tiles[coordinate] = True

def expand_field(tiles):
    # return a tile dictionary that is expanded with 1.
    for tile in dict(tiles):
        x = int(tile.split(';')[0])
        y = int(tile.split(';')[1])
        # do not expand from white tiles.
        if not tiles[tile]:
            for direction in directions:
                adjacent_coordinate = str(x + directions[direction][0])+';'+str(y + directions[direction][1])
                if adjacent_coordinate not in tiles:
                    tiles[adjacent_coordinate] = True

def exhibit_rule(tile):
    x = int(tile.split(';')[0])
    y = int(tile.split(';')[1])
    adjacent_black_count = 0
    # count adjacent black tiles.
    for direction in directions:
        adjacent_coordinate = str(x + directions[direction][0])+';'+str(y + directions[direction][1])
        if adjacent_coordinate in tiles and not tiles[adjacent_coordinate]:
            adjacent_black_count += 1       
    # return tile after exhibit rule is applied. (True = White, False = Black)
    if tiles[tile] and adjacent_black_count == 2:
        # - Any white tile with exactly 2 black tiles immediately adjacent
        #   to it is flipped to black.
        return False
    elif adjacent_black_count not in [1,2] and not tiles[tile]:
        # - Any black tile with zero or more than 2 black tiles immediately adjacent 
        #   to it is flipped to white.
        return True 
    else: 
        return tiles[tile]

### Part One ###
for walk in tilewalks:
    # print(walk)
    steps = []
    step_no = 0
    x = 0
    y = 0
    while step_no < len(walk):
        step = walk[step_no]
        if step == 'e':
            x += 4
        elif step == 'w':
            x -= 4
        else:
            step = walk[step_no:step_no+2]
            step_no += 1
        if step == 'se':
            x += 2
            y -= 3
        elif step == 'sw':
            x -= 2
            y -= 3
        elif step == 'nw':
            x -= 2
            y += 3
        elif step == 'ne':
            x += 2
            y += 3
        coordinate = str(x)+';'+str(y)
        path[coordinate] = [walk_no, step_no, step]
        if coordinate not in tiles:
            tiles[coordinate] = True
        step_no += 1
    else:
        if coordinate in tiles:
            tiles[coordinate] = not(tiles[coordinate])
        else:
            tiles[coordinate] = False
    walk_no +=1

white_count = sum(tiles.values())
black_count = len(tiles) - white_count
print('----part one----\nwhite count: %s (evaluated tiles)\nblack count: %s\n----------------' %(white_count, black_count))

### Part Two ###
flip_tiles = {}
i = 0
while i < 100:
    expand_field(tiles)
    flip_tiles.clear()
    for tile in tiles:
        new_tile = exhibit_rule(tile)
        if new_tile != tile:
            flip_tiles[tile] = new_tile
    # do the flip on all changed tiles when rule has been applied to all relevant tiles.
    for flip in flip_tiles:
        tiles[flip] = flip_tiles[flip]
    i += 1

white_count = sum(tiles.values())
black_count = len(tiles) - white_count

print('--part two--\nwhite count: %s (evaluated tiles)\nblack count: %s' %
      (white_count, black_count))
