from fractions import Fraction

numOps = int(input())

for i in range(numOps):
    op = input().split(' ')
    left = Fraction(int(op[0]), int(op[1]))
    right = Fraction(int(op[3]), int(op[4]))
    if op[2] == '-': 
        result = left - right
    if op[2] == '+': 
        result = left + right
    if op[2] == '/': 
        result = left / right
    if op[2] == '*': 
        result = left * right
    print(result.numerator, '/', result.denominator)