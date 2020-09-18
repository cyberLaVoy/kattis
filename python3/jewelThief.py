
def gatherJewelsInfo(numJewels):
    jewels = [] 
    for i in range(numJewels):
        jewelAttr = input().split(' ')
        size = int(jewelAttr[0])
        value = int(jewelAttr[1])
        jewel = {"size":size, "value":value}
        jewels.append(jewel)
    return jewels

def zeroOneKnapsack(jewels, maxCapacity):
    n = len(jewels)
    m = maxCapacity + 1
    prevRow = [0]*m
    currentRow = [0]*m
    for j in range(m):
        if jewels[0]["size"] <= j:
            prevRow[j] = jewels[0]["value"]
        else:
            prevRow[j] = 0
    for i in range(1, n):
        for j in range(1, m):
            jewelSize = jewels[i]["size"]
            jewelValue = jewels[i]["value"]
            if jewelSize <= j:
                currentRow[j] = max(prevRow[j], jewelValue + prevRow[j-jewelSize])
            else:
                currentRow[j] = prevRow[j]
        prevRow, currentRow = currentRow, prevRow
    return prevRow

def printRow(row):
    for i in range(1, len(row)):
        print(row[i], end=' ')
    print()

def main():
    parameters = input().split(' ')
    numJewels = int(parameters[0])
    maxCapacity = int(parameters[1])
    jewels = gatherJewelsInfo(numJewels)
    bestRow  = zeroOneKnapsack(jewels, maxCapacity)
    printRow(bestRow)
main()

