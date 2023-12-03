__doc__ = '''
day 10
'''
puzzle_input = open("2022/input/day10input.txt", encoding='utf-8').readlines()
puzzle_input_test = open("2022/input/day10inputtest.txt", encoding='utf-8').readlines()
puzzle_input_small_test = '''noop
addx 3
addx -5
'''.splitlines()

register = 1
cycle = 0
part_one_signals = []
img = []

add_value = 1
x = 1
sprite_positions = []

for l in puzzle_input:
    cycle_input = l.split()
    if cycle_input[0] == 'noop':
        cycle += 1
        sprite_positions.append(x)
    else:
        add_value = int(cycle_input[1])
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            part_one_signals.append(register*cycle)
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            part_one_signals.append(register*cycle)
        sprite_positions.append(x)
        sprite_positions.append(x)
        x += add_value
        register += add_value


def render_output(h=6, w=40, on_pixel='#', off_pixel=' ', image_data=None):
    """
    Takes a list of active pixels from left to right, breaks on width (w)
    """
    columns = range(0, w)
    rows = range(0, h)
    left_pad = int(len(str(h))+1)
    header = ['']*2
    for hc in columns:
        header[0] += str(hc)[0] if (hc > 9) else ' '
        header[1] += str(hc)[1] if (hc > 9) else str(hc)[0]
    frame = ''
    for header_row in header:
        frame += ''.rjust(left_pad+1) + header_row + '\n'
    frame += ''.rjust(left_pad)+'.'+'—'*(w+1)+'.\n'
    pixel_position = 0
    for yi in rows:
        row = ''
        for xi in columns:
            row += off_pixel if pixel_position not in image_data else on_pixel
            pixel_position += 1

        frame += f'{str(yi).ljust(left_pad)}| {row}|\n'
    frame += "'".rjust(left_pad+1) + ('—'*(w+1))+"'"
    return frame

for a in range(0, len(sprite_positions), 40):
    for b in range(40):
        if abs(sprite_positions[a + b] - b) <= 1:
            img.append(a+b)

print(f'''
part one signals:   {part_one_signals}
part one answer:    {sum(part_one_signals)}

part two answer:

{render_output(image_data=img)}
''')
