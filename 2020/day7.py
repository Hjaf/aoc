#
# I cheated on part2 because i failed. -1 stars for me :(
#
import re
cargo = open("input/day7input.txt", "r").read().split('\n')
value_child = "shiny gold"
baglist = {}# list() # list of all bags
checklist = {}
sgparents = 0 # count of bags that hold shiny gold bags
totalsgbags = 0

"""
# Dictionary schema
baglist:
[ 
    'bag name': {
        "children":
            {
                (child one, 2), (child two, 5), (child three, 2), (shiny bag, 3)
            },
        "parent": 'parent',
        "count": 3 # count of bags together with shiny gold bags

    }
]

"""

for bags in cargo:
    bag =  re.split("\sbags\scontain\s\d\s|\sbags?\,?\s\d\s", re.sub("\sbags?\.|\sbags\scontain\sno\sother", "", bags))
    value = int(0)
    children = {}
    for chldr in re.findall('\d+\s\w+\s+\w+', bags):
        chld = chldr.split()
        child = chld[1] + ' ' + chld[2]
        child_count = int(chld[0])
        children[child] =  int(chld[0]) # dict of children {'bag name': int(count)}
        if child == value_child:
            value += child_count
    baglist[bag[0]] = {"children": children, "count": value}

#  parent
for bag in baglist:
    for child in baglist[bag].get('children'):
        baglist[child].update({"parent": bag})

counted = {}

value_parents = {}

def countparents(child):
    for b in baglist:
        children = list(baglist[b]['children'])
        if b not in value_parents and child in children:
            countparents(b)
            value_parents[b] = True



def countbags(b, d):
    if b not in counted:
        bag = baglist[b]['children'].items()
        count_all_value = []
        for c, child_count in bag:

            grand_children = countbags(c, d+1)
            
            count_all_value.append(child_count + (child_count * grand_children))
        
        return sum(count_all_value)
    return counted[b]

totalsgbags = countbags(value_child, 0)

countparents(value_child)
sgparents = len(value_parents)


# correct answer check
correct = 0
if sgparents == 274:
    print('\nPart 1 correct')
    correct += 1
print(sgbags)

if totalsgbags == 158730:
    print('\nPart 2 correct')
    correct +=  1
print(totalsgbags)

if correct < 2:
    print('bwap bwaap bwaaaap.')
