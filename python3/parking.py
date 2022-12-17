import sys

def solve():
    params = sys.stdin.readline().strip().split()

    A = int(params[0])
    B = int(params[1])
    C = int(params[2])

    intervals = []
    interval = sys.stdin.readline()
    while interval != '':
        interval = interval.strip().split()
        interval = [int(x) for x in interval]
        intervals.append(interval)
        interval = sys.stdin.readline()

    truckTimes = {1:0, 2:0 ,3:0}
    firstArrivalTime = min(intervals[0][0],intervals[1][0],intervals[2][0])
    lastDepartureTime = max(intervals[0][1],intervals[1][1],intervals[2][1])
    for i in range(firstArrivalTime+1, lastDepartureTime+1):
        numTrucks = 0
        for j in range(len(intervals)):
            if intervals[j][0] < i and intervals[j][1] >= i:
                numTrucks += 1
        if numTrucks != 0:
            truckTimes[numTrucks] += 1
    cost = 1*truckTimes[1]*A+ 2*truckTimes[2]*B+ 3*truckTimes[3]*C
    print(cost)


solve()