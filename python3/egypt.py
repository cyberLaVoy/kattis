import sys

triangle = sys.stdin.readline().strip().split()
triangle = [int(x) for x in triangle]
while not (triangle[0]==0 and triangle[1]==0 and triangle[2]==0):
    triangle.sort()
    if triangle[0]**2+triangle[1]**2 == triangle[2]**2:
        print("right")
    else:
        print("wrong")
    triangle = sys.stdin.readline().strip().split()
    triangle = [int(x) for x in triangle]