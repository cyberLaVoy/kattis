import math 

points = []
for i in range(3):
    point = input().split(' ')
    x = int(point[0])
    y = int(point[1])
    points.append((x, y))

maxDistance = 0
point1 = -1
point2 = -1
for i in range(3):
    for j in range(i+1, 3):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[j][0]
        y2 = points[j][1]
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if distance > maxDistance:
            point1 = points[i]
            point2 = points[j]
            maxDistance = distance
points.remove(point1)
points.remove(point2)
point3 = points[0]
if point1[0] != point3[0] and point2[1] != point3[1]:
    print(point1[0], point2[1])
else:
    print(point2[0], point1[1])

