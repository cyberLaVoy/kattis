
while True:
    numLogs = int(input())
    if numLogs == -1:
        break
    logs = []
    for i in range(numLogs):
        log = input().split()
        log = [int(x) for x in log]
        logs.append(log)
    totalDistance = 0
    prevTime = 0
    for i in range(len(logs)):
        speed = logs[i][0]
        duration = logs[i][1] - prevTime
        distance = speed*duration
        totalDistance += distance
        prevTime = logs[i][1]
    print(totalDistance, "miles")

        