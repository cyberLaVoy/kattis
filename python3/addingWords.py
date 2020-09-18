import sys


def calculate(equation, variables, values):
    string = ""
    for i in range(len(equation)):
        if i & 1 == 1:
            string += equation[i]
        else:
            if equation[i] in variables:
                string += str(variables[equation[i]])
            else:
                return "unknown"
    result = str(eval(string))
    if result in values:
        return values[result]
    else:
        return "unknown"


def solve():
    variables = {}
    values = {}

    line = sys.stdin.readline().strip()
    while line != '':
        line = line.split()
        if line[0] == "def":
            if line[1] in variables:
                del values[variables[line[1]]] # also erase previous value entry
            variables[line[1]] = line[2]
            values[line[2]] = line[1]
        elif line[0] == "calc":
            equation = line[1:]
            for v in equation:
                print(v, end=' ')
            print( calculate(equation[:-1], variables, values) )
        else:
            variables = {}
            values = {}

        line = sys.stdin.readline().strip()

solve()