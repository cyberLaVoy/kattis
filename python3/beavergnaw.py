import math 

params = input().split()
D = int(params[0])
V = int(params[1])
while not (D == 0 and V == 0):

    d = (D**3 - 6*V/math.pi)**(1/3) # just had to get dirty and do this algebra
    print(d)

    params = input().split()
    D = int(params[0])
    V = int(params[1])

