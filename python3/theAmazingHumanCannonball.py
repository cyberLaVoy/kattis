import math

g = 9.81
numTests = int(input())

for i in range(numTests):
    test = input().split()
    test = [float(x) for x in test]
    v0 = test[0]
    theta = test[1]*math.pi/180
    x1 = test[2]
    h1 = test[3]
    h2 = test[4]
    t = x1/(v0*math.cos(theta))
    y1 = v0*t*math.sin(theta)-1/2*g*t**2
    if y1 > h1+1 and y1 < h2-1:
        print("Safe")
    else:
        print("Not Safe")

