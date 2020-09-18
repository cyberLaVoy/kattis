
dice = input().split(' ')

sides1 = int(dice[0])
sides2 = int(dice[1])

maxOutcome = sides1 + sides2
minOutcome = 2

rollResults = [0]*(maxOutcome+1)

for i in range(1, sides1+1):
    for j in range(1, sides2+1):
        result = j+i
        rollResults[result] += 1

maxRollCount = 0
for i in range(len(rollResults)):
    if rollResults[i] > maxRollCount:
        maxRollCount = rollResults[i]

mostProbable = []
for i in range(len(rollResults)):
    if rollResults[i] == maxRollCount:
        mostProbable.append(i)

for i in range(len(mostProbable)):
    print(mostProbable[i])