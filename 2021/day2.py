coursePlan = open('input/day2input.txt','r').readlines()
# coursePlan = open('../input/day2inputexample.txt','r').readlines()
### Part One

distance = int(0)
depth = int(0)
i = 0
for change in coursePlan:
    
    a = change.rstrip().split(' ')
    direction = a[0]
    range = int(a[1])
    if direction == 'up':
        depth -= range
    elif direction == 'down':
        depth += range
    else: 
        distance += range
    i += 1

partOneAns = distance * depth
print(f'''
Part One:
Distance: {distance}
Depth: {depth}
Answer: {partOneAns}
''')

### Part Two

distance = int(0)
depth = int(0)
aim = int(0)
i = 0
for change in coursePlan:
    a = change.rstrip().split(' ')
    direction = a[0]
    range = int(a[1])
    if direction == 'up':
        aim -= range
    elif direction == 'down':
        aim += range
    else:
        distance += range
        depth += range * aim
    i += 1

partTwoAns = depth * distance

print(f'''
Part Two:
Distance: {distance}
Depth: {depth}
Answer: {partTwoAns}
''')
