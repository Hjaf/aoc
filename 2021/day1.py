input = open('input/day1input.txt','r').readlines()
dn = []
for s in input:
    dn.append(int(s))
i = 0
dic = 0
agic = 0
dpg = dn[0:2]
dcg = dn[1:3]
for d in dn:
    if i > 2:
        dpg = dn[i-3:i]
<<<<<<< HEAD
        dcg = dn[i-2:(i+1)]
        if (sum(dpg) < sum(dcg)):
=======
        iCurrentGroup = dn[i-2:(i+1)]
        if (sum(dpg) < sum(iCurrentGroup)):
>>>>>>> d7c7175868c039bb8148ad0701bd7a77e69fdef1
            agic += 1
    if (d > dn[i-1]):
        dic += 1      
    i += 1
print(f'''
Part 1: {dic}
Part 2: {agic}
''')