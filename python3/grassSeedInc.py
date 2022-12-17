

costOfSeed = float(input())
numLawns = int(input())

totalCost = 0
for i in range(numLawns):
    lawnDimensions = input().split(' ')
    lawnWidth = float(lawnDimensions[0])
    lawnHeight = float(lawnDimensions[1])
    totalCost += (lawnWidth*lawnHeight)
totalCost *= costOfSeed

print(totalCost)
