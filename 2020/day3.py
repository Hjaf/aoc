slope = open('day3input.txt', 'r').readlines()


def path(x, y):
    pos = 0
    i = 0
    tree_count = 0
    for slide in slope:
        slope_edge = len(slide.strip())
        if slope_edge <= pos:
            # print('edge reached: %s, edge pos: %s' %(pos, slope_edge))
            pos = pos - slope_edge
            
        if slide[pos] == '#':
            tree_count += 1
        # print('slope slide:\n%sposition: %s, character: %s, slide#: %s\n' %(slide, pos, slide[pos], i))
        pos += x
        i += y
    return tree_count


# part one
print('answer part one: %s' %(path(3, 1)))


