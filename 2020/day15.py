spoken = [6, 4, 12, 1, 20, 0, 16]
i = len(spoken)
def next_number(x, d, th):
    global i
    lsrev = list(reversed(spoken))

    i += 1
    if i == th:
        print('%s the %sth number spoken\ndepth is: %s' %(x, i, d))
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
    
print(next_number(0, 0, 2020))