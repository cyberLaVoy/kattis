
def time(obj):
    time = obj.split()[0].split(':')
    time[0] = str(int(time[0])%12)
    time = time[0] + time[1]
    return int(time)

def printTime(times):
    times.sort(key=time)
    for t in times:
        print(t)
 
    
def solve():
    numTimes = int(input())
    while numTimes != 0:
        amTimes = []
        pmTimes = []
        for i in range(numTimes):
            time = input()
            meridian = time.split()[1]
            if meridian == 'a.m.':
                amTimes.append(time)
            else:
                pmTimes.append(time)
        printTime(amTimes)
        printTime(pmTimes)
        print()

        numTimes = int(input())

solve()