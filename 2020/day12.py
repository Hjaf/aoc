import math
navigation = open('day12input.txt','r').readlines()

# Part one
x = 0
y = 0
instruction = 'E'
heading = 90
for nav in navigation:
    nav = nav.strip()
    instruction = nav[0]
    nav_value = float(nav[1:])
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
        y += nav_value * math.cos(math.radians(heading))
        x += nav_value * math.sin(math.radians(heading))
part_one_answer = abs(x) + abs(y)
print(f'part one answer: {int(part_one_answer)}')

# Part two
def waypoint(position, instruction, nav_value):
    p_x = position[1]
    p_y = position[2]
    x = waypoints[position][0]
    y = waypoints[position][1]
    if x == 0 or y == 0:
        distance = float(max(x, y))
        heading = float(0)
    else:
        distance = round(math.hypot(x, y), 6)
        if y > 0:
            heading = round(math.asin(y/distance), 6)
            if x < 0:
                heading = round(abs(heading - math.radians(180)), 6)
        else:
            heading = round(abs(math.acos(x/distance) - math.radians(360)), 6)
    if instruction == 'R':
        new_heading = heading - math.radians(nav_value)
        x = round(math.cos(new_heading)*distance, 6)
        y = round(math.sin(new_heading)*distance, 6)
    elif instruction == 'L':
        new_heading = heading + math.radians(nav_value)
        x = round(math.cos(new_heading)*distance, 6)
        y = round(math.sin(new_heading)*distance, 6)
    elif instruction == 'N':
        y += nav_value
    elif instruction == 'S':
        y -= nav_value
    elif instruction == 'E':
        x += nav_value
    elif instruction == 'W':
        x -= nav_value
    elif instruction == 'F':
        p_x += x*nav_value
        p_y += y*nav_value
    position = (position[0]+1, p_x, p_y)
    waypoints[position] = [x, y]
    return position

x = float(10)
y = float(1)
p_x = float(0)
p_y = float(0)
i = 0
position = (i, p_x, p_y)
waypoints = {position: [x, y]}

for nav in navigation:
    nav = nav.strip()
    instruction = nav[0]
    nav_value = float(nav[1:])
    position = waypoint(position, instruction, nav_value)

m_dist_item = list(waypoints.keys())[-1]
part_two_answer = int(round(abs(m_dist_item[1])+abs(m_dist_item[2])))
print(f'part two answer: {part_two_answer}')

#
# Had to cheat to arrive at the right answer. I do not understand the math (obviously),
# but it seems I have to round every calculation where heading is involved(using 6-9 decimals). 
# Why I have to use round with min 6 and max 9 decimals to arrive at the correct answer is
# incomprehensible to me
#
