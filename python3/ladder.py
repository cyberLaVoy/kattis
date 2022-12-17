import math

dimensions = input().split(' ')

wallHeight = int(dimensions[0])
greatestAngle = int(dimensions[1])

ladderLength = math.ceil(wallHeight/math.sin(greatestAngle*math.pi/180))
print(ladderLength)