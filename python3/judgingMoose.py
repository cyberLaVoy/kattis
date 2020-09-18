
tines = input().split()
tines = [int(x) for x in tines]

point = 2*max(tines)
isEven = tines[0] == tines[1]

if point == 0:
    print("Not a moose")
elif isEven:
    print("Even", point)
else:
    print("Odd", point)
