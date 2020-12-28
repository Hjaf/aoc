# inumbers = open('day1inputsample.txt','r').readlines()
inumbers = open('day1input.txt','r').readlines()

target_value = 2020

# def candidates(expense):

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
    r_expenses = expenses
    r_expenses.pop(r_expenses.index(x))
    for y in expenses:
        if x + y < target_value:
            print(len(expenses))
            r_expenses.pop(r_expenses.index(y))
            product = x + y
            remaining = target_value - product
            # print(remaining)
            if remaining in r_expenses:
                answer = x * y * remaining 
                print('%s * %s * %s = %s'%(x, y, product, answer))
                return answer
            else:
                r_expenses = expenses

            

for expense in expenses:
    result = product_three(expense)
    if result:
        print('multiplication of 3 values with sum 2020: %s' %(result))