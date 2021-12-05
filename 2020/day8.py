instructions = open("input/day8input.txt", "r").read().split('\n')
i = 0 # final step id / no (string because i use a dictionary)
b = 0 # the number of nop actions in action_list
c = 0 # the number of jmp actions in action_list
modifier = 0 #step at which to modify the action.
part_one_answer = 0 # advent of code answer to part one
part_two_answer = 0 # advent of code answer to part two
attempt = 0 # keeping track of loops
accumulated = 0 # the accumulator value.
instruction_list = {} # list of instructions starting from '1' _identified by strings not integers_

# read input into instruction_list #
for instruction in instructions:
    line = instruction.split()
    if line[0] == "acc" or line[0] == "nop":
        b += 1
    else: 
        c += 1

    i += 1
    instruction_list[str(i)] = [line[0], int(line[1]), 0]

def reset():
    global accumulated
    accumulated = 0 #reset accumulated
    for s in instruction_list:
        step = instruction_list[str(s)]
        action = step[0]
        value = step[1]
        repeat = int(step[2])
        if repeat > 0:
            instruction_list[str(s)] = [action, value, 0] # reset repeats
    return

def boot(s, modifier):
    global part_one_answer
    global part_two_answer
    global accumulated
    global loop_count 
    global attempt
    step = instruction_list[str(s)]
    action = step[0]
    value = step[1]
    repeat = step[2]

    if int(s) >= i:
        print('''
-------------- BOOT COMPLETED ---------------
Accumulated value: %s
Debugging complete after %s attempts
Final step (%s): %s 
---------------------------------------------
        ''' %(accumulated, attempt, s, step))
        part_two_answer = accumulated
        return False
    elif repeat == 1:
        if attempt == 1: 
            part_one_answer = accumulated
            return True
        else: 
            return False

    elif action == 'acc':
        n = int(s) + int(1)
        accumulated += value

    elif action == 'jmp':
        if modifier == s:
            n = int(s) + int(1)
        else: 
            n = int(s) + int(value)

    elif action == 'nop':
        if modifier == s:
            n = str(int(s) + int(value))
        else: 
            n = int(s) + int(1)

    instruction_list[str(s)] = [action, value, repeat+1]
    boot(n, modifier)


for s in list(instruction_list):
    attempt += 1
    step = instruction_list[str(s)] 
    action = step[0]
    if action == 'jmp' or action == 'nop':
        modifier = int(s)
    if boot(1, modifier) == False or part_two_answer > 0:
        break
    else: 
        reset()
        continue


    
print('''
************* Advend of Code *************

Part one answer: %s

Part two answer: %s

******************************************
''' %(part_one_answer, part_two_answer))

