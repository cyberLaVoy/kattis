
case = 1
while True:
    numNames = int(input())
    if numNames != 0:
        print("SET", case)
        case += 1
    else:
        break
    names1 = []
    names2 = []
    for i in range(numNames):
        name = input()
        if i & 1 == 0:
            names1.append(name)
        else:
            names2.append(name)
    names2.reverse()
    for i in range(len(names1)):
        print(names1[i])
    for i in range(len(names2)):
        print(names2[i])




