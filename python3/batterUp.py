
numAtBats = int(input())

atBats = input().split(' ')
atBats = [int(x) for x in atBats]

countedAtBats = numAtBats
numBases = 0
for i in range(numAtBats):
    if atBats[i] == -1:
        countedAtBats -= 1
    else:
        numBases += atBats[i]

print(numBases/countedAtBats)


