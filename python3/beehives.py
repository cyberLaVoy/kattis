import math

params = input().split()
maxDist = float(params[0])
numHives = int(params[1])
while not (maxDist == 0 and numHives == 0):
    sweetHives = [True]*numHives
    hives = []
    for i in range(numHives):
        hive = input().split()
        hive = [float(x) for x in hive]
        hives.append(hive)
    for i in range(len(hives)):
        for j in range(i+1, len(hives)):
            x1 = hives[i][0]
            x2 = hives[j][0]
            y1 = hives[i][1]
            y2 = hives[j][1]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if dist <= maxDist:
                sweetHives[i] = False
                sweetHives[j] = False
    numSweet = 0
    numSour = 0
    for sweet in sweetHives:
        if sweet:
            numSweet += 1
        else:
            numSour += 1
    print(numSour, "sour,", numSweet, "sweet")

    params = input().split()
    maxDist = float(params[0])
    numHives = int(params[1])
