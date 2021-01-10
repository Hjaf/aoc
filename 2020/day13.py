notes = '''1002632
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,829,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,677,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19
'''
# notes = '''939
# 7,13,x,x,59,x,31,19'''

earliest = notes.splitlines()[0].strip()
busses = notes.splitlines()[1].strip().split(',')

# part one
i = 0
wait = True
while wait: #i <= int(earliest):
    for bus in busses:
        if bus != 'x' and i >= int(earliest):
            if (i % int(bus) == 0):
                print(f'time: {i}, bus: {bus}, answer: {(i - int(earliest))*int(bus)}')
                wait = False
    i += 1