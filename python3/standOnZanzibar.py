
numTestCases = int(input())

for i in range(numTestCases):
    turtleCounts = input().split()
    turtleCounts = [int(x) for x in turtleCounts]
    totalAliens = 0
    for i in range(len(turtleCounts)-2):
        if turtleCounts[i+1] > 2*turtleCounts[i]:
            totalAliens += turtleCounts[i+1] - 2*turtleCounts[i]
    print(totalAliens)

