import math

numTests = int(input())

for i in range(numTests):
    numMoves = int(input())
    position = [0,0]
    direction = 90 # in degrees
    for j in range(numMoves):
        move = input().split()
        deltaTheta = float(move[0])
        direction += deltaTheta
        distance = float(move[1])
        deltaX = math.cos(direction*math.pi/180)*distance
        deltaY = math.sin(direction*math.pi/180)*distance
        position[0] += deltaX
        position[1] += deltaY
    print(position[0], position[1])
