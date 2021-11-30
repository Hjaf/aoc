# for testing
sample = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

slope = open('input/day3input.txt', 'r').readlines()
# slope = sample.splitlines()

def path(x, y):
    pos = 0
    i = 0
    tree_count = 0
    while i < len(slope):
        slide =  slope[i]
        slope_edge = len(slide.strip('\n'))
        if slope_edge <= pos:
            pos = pos - slope_edge
        if slide[pos] == '#':
            tree_count += 1
        pos += x
        i += y
    return tree_count


hits = path(3, 1)
# part one
print('answer part one: %s' %(hits))

# part two
vectors = [[1, 1], [5, 1], [7, 1], [1, 2]]

for vector in vectors:
    vector_hits = path(vector[0], vector[1])
    # print('vector: %s results in: %s trees hit' %(vector, vector_hits))
    hits = hits * vector_hits

print('answer part two: %s' %(hits))