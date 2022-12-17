

def move(territory, occupied):
    moved = False
    copyOccupied = []
    for each in range(len(occupied)):
        copyOccupied.append(occupied.pop())
    for spot in copyOccupied:
        i = spot[0]
        j = spot[1]
        if i+1 < len(territory) and territory[i+1][j] == False:
            moved = True
            occupied.append([i+1,j])
            territory[i+1][j] = True
        if i-1 >= 0 and territory[i-1][j] == False:
            moved = True
            occupied.append([i-1,j])
            territory[i-1][j] = True
        if j+1 < len(territory[0]) and territory[i][j+1] == False:
            moved = True
            occupied.append([i,j+1])
            territory[i][j+1] = True
        if j-1 >= 0 and territory[i][j-1] == False:
            moved = True
            occupied.append([i,j-1])
            territory[i][j-1] = True
    return moved

def conquer(territory, occupied):
    days = 1
    for spot in occupied:
        territory[spot[0]][spot[1]] = True
    while move(territory, occupied):
        days += 1
    return days

def solve():
    params = input().split()

    numRows = int(params[0])
    numCols = int(params[1])
    numSpots = int(params[2])

    territory = []
    for i in range(numRows):
        territory.append([False]*numCols)

    occupied = []
    for i in range(numSpots):
        spot = input().split()
        spot = [int(x)-1 for x in spot]
        occupied.append(spot)
    print(conquer(territory, occupied))
solve()
