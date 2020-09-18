

numGroups = int(input())

for j in range(numGroups):
    group = input().split(' ')
    group = [int(x) for x in group]
    currentNumber = group[1]
    for i in range(1, len(group)-1):
        if group[i] != currentNumber:
            print(i)
            break
        currentNumber += 1
