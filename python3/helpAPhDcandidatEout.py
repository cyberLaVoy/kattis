
numTests = int(input())

for i in range(numTests):
    equation = input()
    if equation == "P=NP":
        print("skipped")
    else:
        equation = equation.split('+')
        a = int(equation[0])
        b = int(equation[1])
        print(a+b)