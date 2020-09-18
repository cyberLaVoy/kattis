
input()
temps = [int(x) for x in input().split()]

bestDay = 1
bestMax = max(temps)

for i in range(1,len(temps)-1):
    maxTemp = max(temps[i-1], temps[i+1])
    if maxTemp < bestMax:
        bestDay = i
        bestMax = maxTemp

print(bestDay, bestMax)
