import sys

variables = {}
line = sys.stdin.readline().strip()
while line != '':
    line = line.split()
    if line[0] == "define":
        value = int(line[1])
        label = line[2]
        variables[label] = value
    elif line[0] == "eval":
        left = line[1]
        right = line[3]
        operand = line[2]
        if left not in variables or right not in variables:
            print("undefined")
        elif operand == '=':
            print(str(variables[left] == variables[right]).lower())
        elif operand == '>':
            print(str(variables[left] > variables[right]).lower())
        elif operand == '<':
            print(str(variables[left] < variables[right]).lower())
    line = sys.stdin.readline().strip()