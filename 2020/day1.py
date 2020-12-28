inumbers = open('day1input.txt','r').readlines()

target_value = 2020
expenses = []
answer = False

for rnum in inumbers:
    num = int(rnum.strip())
    expenses.append(num)
    for ronum in inumbers:
        onum = int(ronum.strip()) 
        num_sum = num + onum
        # solve only once. but continue array collection 
        if num_sum == 2020 and onum != num and not answer:
            answer = num * onum
            print('numbers: %s + %s = %s \nmultiplied: %s' % (num, onum, num_sum, answer))
           
def product_three(x):
    r_expenses = list(expenses)
    r_expenses.pop(r_expenses.index(x))
    for y in r_expenses:
        if x + y < target_value:
            r_expenses.pop(r_expenses.index(y))
            product = x + y
            remaining = target_value - product
            # print(remaining)
            if remaining in r_expenses:
                answer = x * y * remaining 
                return str.format('%s * %s * %s = %s'%(x, y, product, answer))
                # break
            else:
                r_expenses.append(y)

            

for expense in expenses:
    result = product_three(expense)
    if result:
        print('multiplication of 3 values with sum 2020:\n %s' %(result))
        break