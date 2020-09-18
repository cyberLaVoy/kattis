

def triangleArea(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c 
    return abs( (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) ) / 2

def getPoint():
    point = input().split()
    point = (int(point[0]), int(point[1]))
    return point

def main():
    orig1 = getPoint()
    orig2 = getPoint()
    orig3 = getPoint()
    origArea = triangleArea(orig1, orig2, orig3)

    numPoints = int(input())
    numInside = 0
    for _ in range(numPoints):
        area = 0 
        point = getPoint()
        area += triangleArea(orig1, orig2, point)
        area += triangleArea(orig1, orig3, point)
        area += triangleArea(orig2, orig3, point)
        if area == origArea:
            numInside += 1
    print(origArea)
    print(numInside)

main()