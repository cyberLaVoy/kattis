import math

pattern = []
for i in range(3):
    row = input().split()
    row = [int(x) for x in row]
    pattern.append(row)

length = 0
for i in range(1,9):
    currLocation = []
    nextLocation = []
    for j in range(len(pattern)):
        for k in range(len(pattern)):
            if pattern[j][k] == i:
                currLocation.append(j)
                currLocation.append(k)
            elif pattern[j][k] == i+1:
                nextLocation.append(j)
                nextLocation.append(k)
    length += math.sqrt((nextLocation[0]-currLocation[0])**2+(nextLocation[1]-currLocation[1])**2)
print(length)