import math

numTests = int(input())

for i in range(numTests):
    input() # throw away n
    storeLocations = input().split()
    storeLocations = [int(x) for x in storeLocations]
    storeLocations.sort()
    optimalLocation = sum(storeLocations)/len(storeLocations)
    totalDistance = abs(optimalLocation - storeLocations[0])
    for j in range(len(storeLocations)-1): 
        totalDistance += abs(storeLocations[j] - storeLocations[j+1])
    totalDistance += abs(optimalLocation - storeLocations[len(storeLocations)-1])
    print(int(totalDistance))