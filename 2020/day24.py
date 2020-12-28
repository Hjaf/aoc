tilewalks = open('day24input.txt', 'r').readlines()
# tilewalks = ["nwwswee"]
##
# hexagonal grid 4 by 3, 
# center x distance is 4 
# center y distance is 3
# center diagonal distance is 5 
# (2(x) + 3(y)) 
##
# directions = {'e': [1,0], 'se': [1,-1], 'sw': [-1,-1], 'w': [-1,0], 'nw': [-1,1],'ne': [1,1]}
step_no = 0
walk_no = 0
path = {}
tile = {}
coordinate = '0;0'
path[coordinate] = {walk_no, step_no, ''}
tile[coordinate] = True
for walk in tilewalks:
    # print(walk)
    steps = []
    step_no = 0
    x = 0
    y = 0
    while step_no < len(walk):
        # print('---\nstep: %s' %(step_no))
        step = walk[step_no]
        if step == 'e':
            x += 4
        elif step == 'w':
            x -= 4
        else:
            step = walk[step_no:step_no+2]
            # print('2char step..%s' %(step))
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
        # print('step: %s, to coordinate: %s' %(step, coordinate))
        path[coordinate] = [walk_no, step_no, step]
        step_no += 1
    else:
        # register the tile and flip it if it exists.
        # print('path final coordinate: %s' %(coordinate))
        if coordinate in tile:
            # print('tile %s, %s is flipped! is white: %s' %
            #       (x, y, tile[coordinate]))
            tile[coordinate] = not(tile[coordinate])
        else:
            tile[coordinate] = False
    walk_no +=1
white_count = 0
black_count = 0

for t in tile.values():
    # print(t)
    if t:
        white_count += 1
    else:
        black_count += 1

print('white count: %s\nblack count: %s' %(white_count, black_count))
