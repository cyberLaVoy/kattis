import math

dimensions = input().split()

R = int(dimensions[0])
C = int(dimensions[1])

wholeArea = math.pi*R**2
bodyArea = math.pi*(R-C)**2

print(bodyArea/wholeArea*100)