import math
numCases = int(input())

for i in range(numCases):
    case = input().split()
    b = float(case[0])
    p = float(case[1])
    x = 60/p
    BPM = x*b
    minABPM = BPM - x
    maxABPM = BPM + x
    print(minABPM, BPM, maxABPM)