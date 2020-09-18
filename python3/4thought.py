
#targets = {}
#operators = ['+', '-', '*', '//']
#for i in range(len(operators)):
#    first = operators[i]
#    for j in range(len(operators)):
#        second = operators[j]
#        for k in range(len(operators)):
#            third = operators[k]
#            equation = '4 ' + first + ' 4 ' + second + ' 4 ' + third + ' 4'
#            key = eval(equation)
#            equation += ' = ' + str(key)
#            targets[key] = equation
#print(str(targets).replace('//', '/'))

targets = {16: '4 / 4 * 4 * 4 = 16', 8: '4 / 4 * 4 + 4 = 8', 24: '4 * 4 + 4 + 4 = 24', 9: '4 / 4 + 4 + 4 = 9', 0: '4 / 4 / 4 / 4 = 0', -8: '4 - 4 * 4 + 4 = -8', 7: '4 - 4 / 4 + 4 = 7', 68: '4 * 4 * 4 + 4 = 68', 1: '4 / 4 * 4 / 4 = 1', 4: '4 / 4 / 4 + 4 = 4', -16: '4 - 4 * 4 - 4 = -16', -1: '4 - 4 / 4 - 4 = -1', -60: '4 - 4 * 4 * 4 = -60', 32: '4 * 4 + 4 * 4 = 32', 17: '4 / 4 + 4 * 4 = 17', 15: '4 * 4 - 4 / 4 = 15', 60: '4 * 4 * 4 - 4 = 60', 256: '4 * 4 * 4 * 4 = 256', 2: '4 / 4 + 4 / 4 = 2', -7: '4 / 4 - 4 - 4 = -7', -15: '4 / 4 - 4 * 4 = -15', -4: '4 / 4 / 4 - 4 = -4'}

numTests = int(input())

for i in range(numTests):
    target = int(input())
    if target in targets:
        print(targets[target])
    else:
        print("no solution")
