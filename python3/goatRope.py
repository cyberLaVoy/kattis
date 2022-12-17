import math

def minDistance(corners, post):
    distances = []
    for corner in corners:
        distance = math.sqrt((corner[0]-post[0])**2 + (corner[1]-post[1])**2) 
        distances.append(distance)
    return min(distances)


def solve():
    params = input().split()
    x = int(params[0])
    y = int(params[1])
    x1 = int(params[2])
    y1 = int(params[3])
    x2 = int(params[4])
    y2 = int(params[5])

    post = [x,y]
    corner1 = [x1,y1]
    corner2 = [x2,y2]
    corner3 = [x2,y1]
    corner4 = [x1,y2]

    corners = [corner1,corner2,corner3,corner4]

    topY = max(y1, y2)
    bottomY = min(y1, y2)
    rightX = max(x1, x2)
    leftX = min(x1, x2)

    distance = 0
    if y >= topY and x >= leftX and x <= rightX:
        distance = y - topY
    elif y <= bottomY and x >= leftX and x <= rightX:
        distance = bottomY - y
    elif x >= rightX and y >= bottomY and y <= topY:
        distance = x - rightX
    elif x <= leftX and y >= bottomY and y <= topY:
        distance = leftX - x
    else:
        distance = minDistance(corners, post)
    print(distance)
solve()