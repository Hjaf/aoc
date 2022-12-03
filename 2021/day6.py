from os import chdir, path, sys
abspath = path.abspath(__file__)
cwd = path.dirname(abspath)
chdir(cwd)

if sys.argv.__len__() > 1:
    days = int(sys.argv[1].lower())
else:
    days = 80

input = open('input/day6input.txt', 'r').read()
# input_example = open('input/day6inputexample.txt', 'r').read()


def load_data(input):
    items = input.split(',')
    item_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for item in items:
        item_value = int(item)
        if item_value in item_dict.keys():
            item_dict[item_value] += 1
        else:
            item_dict[item_value] = 1
    return item_dict


lantern_fish_count = load_data(input)


def evolve(fish_count):
    return {
        0: fish_count[1],
        1: fish_count[2],
        2: fish_count[3],
        3: fish_count[4],
        4: fish_count[5],
        5: fish_count[6],
        6: fish_count[7] + fish_count[0],
        7: fish_count[8],
        8: fish_count[0]
    }


day = 0
while day < days:
    lantern_fish_count = dict(evolve(lantern_fish_count))
    day += 1

print(
    f'There are {sum(list(lantern_fish_count.values()))} lanternfish after {days} days!')
