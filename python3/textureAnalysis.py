
line = input()
case = 1
while line != "END":
    distance = 0
    if len(line) != 1:
        i = 1
        while line[i] != '*': 
            distance += 1
            i += 1
    space = 0
    even = True
    for i in range(1, len(line)):
        if line[i] == '*':
            if space < distance:
                even = False
                break
            space = 0
        else:
            space += 1
        if space > distance:
            even = False
            break
    if even:
        print(case, "EVEN")
    else:
        print(case, "NOT EVEN")


    line = input()
    case += 1
