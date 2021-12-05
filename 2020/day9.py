stream = open("input/day9input.txt", "r").read().split('\n')
vstream = []
for s in stream:
    vstream.append(int(s))

match_values = {}
non_match_values = {}
i = 0
i_max = len(vstream)

def find_combination(i, value):
    ivs = i # start at line
    # vs_value = vstream[i] # start line value
    if i_max <= i:
        return False
    batch = vstream[i:]
    loop_batch = []
    vs_sum = 0
    while vs_sum < value:
        # print(min(vstream[i:ivs]))
        # vs_sum += batch[ivs]
        loop_batch.append(batch[ivs])
        vs_low = min(loop_batch)
        vs_high = max(loop_batch)
        vs_low_high_sum = vs_low + vs_high
        vs_sum = sum(loop_batch)
        if vs_sum == value: # and i < ivs:
            # vs_low_value
            # vs_low_high_value = vs_low_value + vs
            info = str('''
***Series (ansver part 2)***
a matching series that has been found.
target was %s
it starts at position %s
and ends at position %s          
low value: %s
high value: %s
low + high = %s
            ''' %(value, i, ivs, vs_low, vs_high, vs_low_high_sum))
            print(info)
            return True
        # #Debug info
        # elif vs_sum > value: 
        #     print('''
        #     exceeded the goal.
        #     target value: %s
        #     final value : %s
        #     it starts at position %s
        #     and ends at position  %s          
        #     low value:  %s
        #     high value: %s
        #     ''' %(value, vs_sum, i, ivs, vs_low, vs_high))
        ivs += 1
    else: 
        return find_combination(i+1, value)

for v in vstream:
    if i <= 25:
        bstart = 0
        bend = i-1
    else:
        bstart = i-25
        bend = i
    if i == 0:
        bend = 0
    batch_start = vstream[bstart]
    batch_end = vstream[bend]
    batch = vstream[bstart:bend]
    info = str('''
Found XMAS weakness (answer part 1):
line: %s 
value: %s
batch first value: %s,
batch last value: %s,
batch length(should be 25): %s
batch:
%s
    ''' %(i, v, batch_start, batch_end, len(batch), batch))

    find_series = False
    combination_not_found = True
    for b in batch:
        for sb in batch:
            if b + sb == v:
                match_values[v] = info
                combination_not_found = False

    if combination_not_found:
        if i > 25:
            print(info)
            non_match_values[v] = info
            find_series = find_combination(0, v)
        
    if find_series:
        break
    i += 1
