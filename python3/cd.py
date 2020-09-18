import sys

lineIndex = 0
lines = sys.stdin.readlines()
params = lines[lineIndex].strip().split()
lineIndex += 1
params = [int(x) for x in params]
while not (params[0] == 0 and params[1] == 0):
    bothOwnCount = 0
    largestCollection = max(params[0], params[1])
    matches = [False]*(1000000000+1)
    for i in range(params[0]):
        cdId = int(lines[lineIndex].strip())
        lineIndex += 1
        matches[cdId] = True
    for i in range(params[1]):
        cdId = int(lines[lineIndex].strip())
        lineIndex += 1
        if matches[cdId]: 
            bothOwnCount += 1
    print(bothOwnCount)

    params = lines[lineIndex].strip().split()
    lineIndex += 1
    params = [int(x) for x in params]

