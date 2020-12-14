
ifile = 'day14input.txt'
# ifile = 'day14inputexample.txt'
ifile = 'day14inputexample2.txt'
instructions = list(open(ifile, "r").read().split('\n'))


mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
memory= {}
memory_version_two = {}

# def maskvariations(variation):
#     b = [0, 1]
#     for x in variation:
    

def maskupdate(madr, mask, patch):
    i = 0
    base = []
    base_two = []
    for c in patch: base.append(c)
    for m in mask:
        if m == '0':
            base_two.append(base[i])
        if m != 'X':
            base[i] = m
        else:
            base_two.append(m)
        i += 1

    memory_version_two[madr] = ''.join(base_two)
    return ''.join(base)


for row in instructions:
    inp = row.split(' = ')
    ival = inp[1]
    if inp[0] == 'mask':
        mask = ival
    else:
        madr = int(inp[0].split('[', 1)[1][:-1])
        b_madr = bin(madr)[2:]                 #pointless00
        sb_madr = str(b_madr).zfill(len(mask)) #pointless
        ival = int(inp[1])
        b_ival = bin(ival)[2:]
        sb_ival = str(b_ival).zfill(len(mask))
        bi = 0
        memory[madr] = maskupdate(madr, mask, sb_ival)
        b_oval = int((memory[madr]), 2)
        debug = str('''
        memory:     %s (addr) = %s (value) \t\t\t(integers)
        patch:      %s
        mask:       %s \t(string)
        memory val: %s \t(memory value)
        patched:    %s \t
        ''' % (madr, ival, sb_ival, mask, memory[madr], b_oval))
        # print(debug)

memory_sum = 0
for mem in list(memory.values()):

    memory_sum += int(mem, 2)
print(memory_sum)

# for mem_two in list(memory.values()):



# print(memory_version_two)

