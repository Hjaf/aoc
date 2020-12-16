spoken = [6, 4, 12, 1, 20, 0, 16]
def next_number(x, d, th):
    lsrev = list(reversed(spoken))
    i = len(spoken)+1
    if i == th:
        print('%s the %sth number spoken\ndepth is: %s' % (x, i, d))
        return x
    elif x in spoken:        
        if x == spoken[-1]:
            ls = 1
        else:
            ls = lsrev.index(x)+1
    else:
        ls = 0
    spoken.append(x)
    return next_number(ls, d+1, th) 


print('\n---- part one ----\n')

print(next_number(0, 0, 2020))

print('\n---- part two ----\n')
spoken = [6, 4, 12, 1, 20, 0, 16]
# find the 30000000th word spoken.
# this will recurse to much using method in part one.
    
spoken_index = {}
i = 0
for num in spoken: 
    spoken_index[num] = len(spoken)

def next_number_two(x, d, th):
    global spoken_index
    # i = len(spoken)+1
        # print('th is %s' %(th))
    if i == th:
        print('%s the %sth number spoken\ndepth is: %s' % (spoken_index[x], i, d))
        return True
    
    spoken.append(x)

    if x in spoken_index:  
        w = abs((len(spoken) - spoken_index[x]))
        print('''
        %s existing at index: %s 
        position of previous: %s
        length of list is   : %s
        - position :        : %s 
         (which is %s steps back)
        ----

        ''' % (x, spoken_index[x], w, len(spoken), spoken_index[x], w))
        nn = str(next_number_two(w, d+1, th))
        print(nn)
        spoken_index[str(nn)] = i
        spoken.append(spoken_index[str(nn)])
        return spoken_index[str(nn)]
    else:
        spoken_index[0] = i
     
    # y = next_number_two(x, d+1, th)
    # print('next number y is:  %s' %(y))
    # spoken_index[y] = i
    # else:
    # y = spoken_index[next_number_two(x, d+1, th)] = i
    spoken_index[x] = len(spoken)-1
    return x
        # spoken.append(x)
    

next_number_two(0, 0, 20)
# print(next_number_two(0,0,2020))
print(spoken)
print(spoken_index)
