f = open("day6input.txt", "r")
gans = f.read().split('\n\n')
pyes = 0 # passenger yes
gyes = 0 # gyes
grpans = []
for ans in gans:
    gcl = list(set())
    pcl.clear()
    for a in ans.split('\n'):
        cset = set()
        for l in a:
            for c in l:
                pcl.append(c)
                cset.add(c)
            gcl.append(cset)
    gyes += len(set.intersection(*gcl))
    pyes += len(set(pcl))


print(pyes)
print(gyes)
