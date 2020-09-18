import math

def criticalPoints(x, y):
    critPts = []
    # derivative coefficients
    a = 12
    b = -4*(x+y)
    c = x*y
    # quadratic formula
    h1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    h2 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    critPts.append(h1)
    critPts.append(h2)
    return critPts

def findMaxVolume(x, y):
    critPts = criticalPoints(x, y)
    maxHeight = min(x, x)/2
    validPts = []
    for v in critPts:
        if v != maxHeight and v != 0:
            validPts.append(v)
    maxVolume = 0
    for v in validPts:
        h = v
        volume = x*y*h-2*x*h**2-2*y*h**2+4*h**3
        if volume > maxVolume:
            maxVolume = volume
    return maxVolume

def solve():
    numBoxes = int(input())

    for i in range(numBoxes):
        dimensions = input().split()
        x = int(dimensions[0])
        y = int(dimensions[1])
        print(findMaxVolume(x,y))
solve()


