import sys, math

dimens = sys.stdin.readline().strip()
while dimens != '':

    dimens = dimens.split()
    radius = float(dimens[0])
    strikeX = float(dimens[1])
    strikeY = float(dimens[2])

    distanceFromCenter = math.sqrt(strikeX**2 + strikeY**2)
    if distanceFromCenter >= radius:
        print("miss")
    else:
        theta = math.acos(distanceFromCenter/radius)
        totalArea = math.pi*radius**2
        smallArea = (radius**2/2)*(2*theta-math.sin(2*theta)) # had to look this area calulation up
        largeArea = totalArea-smallArea
        print(largeArea, smallArea)

    dimens = sys.stdin.readline().strip()