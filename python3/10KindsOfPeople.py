import sys
sys.setrecursionlimit(1000000000)

def gatherLayout(numRows, numCols, lines):
    layout = []
    for i in range(numRows):
        row = lines.pop()
        row = [int(l) for l in row]
        layout.append(row)
    return layout

def gatherMoves(numMoves, lines):
    moves = []
    for i in range(numMoves):
        move = lines.pop().split()
        move = [int(x)-1 for x in move]
        start = ( move[0], move[1] )
        end = ( move[2], move[3] )
        move = {"from":start, "to":end}
        moves.append(move)
    return moves

def fill(layout, i, j, searchValue):
    coordinates = [] 
    fillR(layout, i, j, searchValue, coordinates)
    return coordinates
def fillR(layout, i, j, searchValue, coordinates):
    coordinates.append( (i, j) )
    layout[i][j] = 2
    if i+1 < len(layout) and layout[i+1][j] == searchValue:
        fillR(layout, i+1, j, searchValue, coordinates)
    if i-1 >= 0  and layout[i-1][j] == searchValue:
        fillR(layout, i-1, j, searchValue, coordinates)
    if j+1 < len(layout[i]) and layout[i][j+1] == searchValue:
        fillR(layout, i, j+1, searchValue, coordinates)
    if j-1 >= 0 and layout[i][j-1] == searchValue:
        fillR(layout, i, j-1, searchValue, coordinates)

#  returns a dict of connected components
def findCoordinates(layout, searchValue):
    coordinates = {}
    ccNum = 0
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == searchValue:
                coordinates[ccNum] = fill(layout, i, j, searchValue)
                ccNum += 1
    return coordinates

def describeCoordinates(zeroCoordinates, oneCoordinates):
    coordinates = {}
    for cc in zeroCoordinates:
        for coor in zeroCoordinates[cc]:
            description = {"region": 0, "ccNum": cc}
            coordinates[coor] = description
    for cc in oneCoordinates:
            for coor in oneCoordinates[cc]:
                description = {"region": 1, "ccNum": cc}
                coordinates[coor] = description
    return coordinates

def solve():
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    lines.reverse()
    params = lines.pop().split()
    rows = int(params[0])
    cols = int(params[1])
    layout = gatherLayout(rows, cols, lines)
    numMoves = int(lines.pop())
    moves = gatherMoves(numMoves, lines)

    zeroCoordinates = findCoordinates(layout[:], 0) 
    oneCoordinates = findCoordinates(layout[:], 1)  
    coordinates = describeCoordinates(zeroCoordinates, oneCoordinates)

    for move in moves:
        startRegion = coordinates[move["from"]]["region"]
        startCC = coordinates[move["from"]]["ccNum"]
        endRegion = coordinates[move["to"]]["region"]
        endCC = coordinates[move["to"]]["ccNum"]
        if startRegion == endRegion and startCC == endCC:
            if startRegion == 0:
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")

solve()

