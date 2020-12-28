# inumbers = open('day1inputsample.txt','r').readlines()
inumbers = open('day1input.txt','r').readlines()

for rnum in inumbers:
    num = int(rnum.strip())
    for ronum in inumbers:
        onum = int(ronum.strip()) 
        num_sum = num + onum
        if num_sum == 2020 and onum != num:
            onum_sum = num * onum
            print('numbers: %s + %s = %s \nmultiplied: %s' % (num, onum, num_sum, onum_sum))
