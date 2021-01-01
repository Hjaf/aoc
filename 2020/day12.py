import math
navigation = open('day12input.txt','r').readlines()

x = 0
y = 0
instruction = 'E'
heading = 90
for nav in navigation:
    nav = nav.strip()
    print(f'{nav} - instruction: {nav[0]} nav_value: {nav[1:]}, heading: {heading}')
    instruction = nav[0]
    nav_value = int(nav[1:])
    if instruction == 'R':
        heading += nav_value
    elif instruction == 'L':
        heading -= nav_value
    elif instruction == 'N':
        y += nav_value
    elif instruction == 'S':
        y -= nav_value
    elif instruction == 'E':
        x += nav_value
    elif instruction == 'W':
        x -= nav_value
    elif instruction == 'F':
        y += nav_value * int(math.cos(math.radians(heading)))
        x += nav_value * int(math.sin(math.radians(heading)))

print(abs(x) + abs(y))
