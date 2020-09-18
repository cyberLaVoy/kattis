import math

def inCircle(circleX, circleY, r, pnt):
    distance = math.sqrt((circleY-pnt[1])**2 + (circleX-pnt[0])**2)
    if r >= distance:
        return True

def inRect(topRightX, topRightY, bottomLeftX, bottomLeftY, pnt):
    x = pnt[0]
    y = pnt[1]
    if x > topRightX or x < bottomLeftX:
        return False
    if y > topRightY or y < bottomLeftY:
        return False
    return True

def solve():
    numShapes = int(input())
    shapes = []
    for i in range(numShapes):
        shape = input().split()
        shapes.append(shape)

    numPts = int(input())
    for i in range(numPts):
        pnt = input().split()
        pnt = [int(x) for x in pnt]
        numHits = 0
        for shape in shapes:
            if shape[0] == "circle":
                x = int(shape[1])
                y = int(shape[2])
                r = int(shape[3])
                if inCircle(x,y,r,pnt):
                    numHits += 1
            else:
                x1 = int(shape[3])
                y1 = int(shape[4])
                x2 = int(shape[1])
                y2 = int(shape[2])
                if inRect(x1,y1,x2,y2,pnt):
                    numHits += 1
        print(numHits)

solve()

