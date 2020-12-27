ifile = "day18input.txt"
math_quiz = list(open(ifile, 'r').read().split('\n'))

# for quiz in math_quiz:
#     parenthesis = False
#     for i in quiz: 
#         if 


def calculate(quiz, d):
    # print('---\nquiz: %s\ndepth: %s\n---\n' %(quiz, d))
    i = 0
    pi = 0
    ans = 0
    print(len(quiz))
    while i < len(quiz):
        if quiz[i].isdigit():
            ans = int(quiz[i])
            # print('digit: %s' %(ans))
        elif quiz[i] == '*':
            # print('multiply with %s' %(quiz[i+1:]))
            ans = ans * calculate(quiz[i+1:], d+1)
        elif quiz[i] == '+':
            # print('addition with %s' % (quiz[i+1:]))
            ans = ans + calculate(quiz[i+1:], d+1)
        elif quiz[i] == '(':
            pi = i + quiz[i:].index(')')
            # print('calculate: %s from index %s to index %s' %(quiz[i+1:pi+1], i+1, pi+1))
            #i = pi-1
            return ans + calculate(quiz[i+1:pi+1], d+1)
        # else: 
        #     return ans
        i += 1
    # print('returning: %s from quiz: %s\ndepth: %s\n-----\n\n-----' %(ans, quiz, d))
    return ans


qtest = '1 + 2 * 3 + 4 * 5 + 6'.split()
qtestb = list('1 + (2 * 3) + (4 * (5 + 6))'.replace(' ', ''))
print(qtestb)
# print(qtest)
print(calculate(qtestb, 0))

# print('add %s %s %s = %s' %(ans, quiz[i], quiz[i+1], (ans + int(quiz[i+1]))))
