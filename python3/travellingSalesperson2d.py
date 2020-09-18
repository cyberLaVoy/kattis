import math

def dist(points, i , j):
    x1 = points[i][0]
    x2 = points[j][0]
    y1 = points[i][1]
    y2 = points[j][1]
    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return dist

def greedyTour(points, n):
    used = [False]*n
    tour = [-1]*n
    tour[0] = 0
    used[0] = True
    for i in range(1, n):
        best = -1
        for j in range(1, n):
            if not used[j] and (best == -1 or dist(points, tour[i-1],j) < dist(points, tour[i-1],best)):
                best = j
        tour[i] = best
        used[best] = True
    return tour

def gatherPoints(n):
    points = []
    for i in range(n):
        point = input().split()
        point = [float(x) for x in point]
        points.append(point)
    return points

def main():
    n = int(input())
    points = gatherPoints(n)
    tourIndexes = greedyTour(points, n)
    for index in tourIndexes:
        print(index)

if __name__ == "__main__":
    main()
