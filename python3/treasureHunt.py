

def solve():
    params = input().split()

    rows = int(params[0])
    cols = int(params[1])

    playingArea = []
    explored = []
    for i in range(rows):
        exploredRow = [False]*cols
        explored.append(exploredRow)
        row = input()
        row = [l for l in row]
        playingArea.append(row)

    i = 0
    j = 0
    numSteps = 0
    while True:
        s = playingArea[i][j]
        if explored[i][j]:
            print("Lost")
            break
        explored[i][j] = True
        if s == 'T':
            print(numSteps)
            break
        elif s == 'N':
            i-=1
        elif s == 'S':
            i+=1
        elif s == 'E':
            j+=1
        elif s == 'W':
            j-=1
        if i >= rows or i < 0 or j >= cols or j < 0:
            print("Out")
            break
        numSteps += 1
solve()

