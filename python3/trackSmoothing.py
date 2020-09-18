import math

def findDistance(numPoints):
    points = []
    for i in range(numPoints):
        points.append(input().split())
    points = [ (int(x), int(y)) for x, y in points ]
    distance = 0
    for i in range(len(points)-1):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[i+1][0]
        y2 = points[i+1][1]
        distance += math.sqrt( (x1-x2)**2 + (y1-y2)**2  )
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[-1][0]
    y2 = points[-1][1]
    distance += math.sqrt( (x1-x2)**2 + (y1-y2)**2  )
    return distance 
    
def printFactor(distance, radius):
    factor = round( (distance - 2*math.pi*radius)/distance, 6 )
    if factor < 0:
        factor = "Not possible"
    print(factor)

def main():
    numTests = int(input()) 
    for i in range(numTests):
        params = input().split()
        radius, numPoints = int(params[0]), int(params[1]) 
        distance = findDistance(numPoints)
        printFactor(distance, radius) 
main()