def gatherJewelsInfo(numJewels):
    jewels = [] 
    for i in range(numJewels):
        jewelAttr = input().split(' ')
        size = int(jewelAttr[0])
        value = int(jewelAttr[1])
        jewel = {"size":size, "value":value}
        jewels.append(jewel)
    return jewels

def createMatrix(n,m):
    matrix = []
    for i in range(n):
        matrix.append([-1]*m)
    return matrix
def fillBaseCase(jewels,matrix,n,m):
    for i in range(n):
        matrix[i][0] = 0
    for j in range(m):
        if jewels[0]["size"] <= j:
            matrix[0][j] = jewels[0]["value"]
        else:
            matrix[0][j] = 0

def zeroOneKnapsack(jewels, maxCapacity):
    n = len(jewels)
    m = maxCapacity + 1
    matrix = createMatrix(n, m)
    fillBaseCase(jewels, matrix, n, m)
    for j in range(1, m):
        print(knapsackR(n,j,jewels,matrix), end=' ')
    print()
def knapsackR(i, j, jewels, matrix):
    if matrix[i-1][j] != -1:
        return matrix[i-1][j]
    jewelSize = jewels[i-1]["size"]
    jewelValue = jewels[i-1]["value"]
    if jewelSize <= j:
        matrix[i-1][j] = max(knapsackR(i-1,j,jewels,matrix), jewelValue + knapsackR(i-1,j-jewelSize,jewels,matrix))
        return matrix[i-1][j] 
    else:
        matrix[i-1][j] = knapsackR(i-1,j,jewels,matrix)
        return matrix[i-1][j] 


def printLastRow(knapsackMatrix):
    lastRow = knapsackMatrix[-1]
    for i in range(1, len(lastRow)):
        print(lastRow[i], end=' ')
    print()

def main():
    parameters = input().split(' ')
    numJewels = int(parameters[0])
    maxCapacity = int(parameters[1])
    jewels = gatherJewelsInfo(numJewels)
    zeroOneKnapsack(jewels, maxCapacity)
    #printLastRow(knapsackMatrix)
main()
