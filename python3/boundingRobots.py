

roomDimensions = input().split()
width = int(roomDimensions[0])
height = int(roomDimensions[1])

while not (width == 0 and height == 0):
    numMoves = int(input())
    moves = []
    for i in range(numMoves):
        move = input().split()
        move = {"direction":move[0], "amount":int(move[1])}
        moves.append(move)
    actualX = 0
    actualY = 0
    thinksX = 0
    thinksY = 0
    for i in range(len(moves)):
        direction = moves[i]["direction"]
        amount = moves[i]["amount"]
        if direction in "dl":
            amount = 0 - amount
        if direction in "ud":
            actualY += amount
            if actualY >= height:
                actualY = height-1 
            if actualY < 0:
                actualY = 0
            thinksY += amount
        if direction in "rl":
            actualX += amount
            if actualX >= width:
                actualX = width-1 
            if actualX < 0:
                actualX = 0
            thinksX += amount
    print("Robot thinks", thinksX, thinksY)
    print("Actually  at", actualX, actualY)
    print()
    
    roomDimensions = input().split()
    width = int(roomDimensions[0])
    height = int(roomDimensions[1])

