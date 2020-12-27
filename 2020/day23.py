cups = list(str(418976235))
iterate = 100
cup_count =  len(cups)
# print(cup_count)
# i=0
# print(abs((3-2)-9))
cup = int(cups[0])
while i < iterate:
    # while p <= cup_count:
    # cup = int(cups[d])
    cup_index = cups.index(str(cup))
    take = cups[cup_index+1: cup_index+4]
    before = cups[:cup_index]
    after = cups[cup_index+4]
    d = cup-1
    dp = cups.index(str(d))
    # print(cups[])
    i += 1
123456789
