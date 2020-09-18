
def solve1():
    currentTime = input().split(':')
    cHour = int(currentTime[0]) 
    cMin = int(currentTime[1]) 
    cSec = int(currentTime[2]) 

    explosionTime = input().split(':')
    eHour = int(explosionTime[0]) 
    eMin = int(explosionTime[1]) 
    eSec = int(explosionTime[2])

    sSec = 0
    while not (eHour == cHour and eMin == cMin and eSec == cSec):
        cSec += 1
        sSec += 1
        if cSec == 60:
            cSec = 0
            cMin += 1
        if cMin == 60:
            cMin = 0
            cHour += 1
        if cHour == 24:
            cHour = 0

    sHour = str(sSec//3600%24)
    sMin = str(sSec//60%60)
    sSec = str(sSec%60)
    if sHour == '0' and sMin == '0' and sSec == '0': # edge case
        sHour = "24"
    while len(sHour) < 2:
        sHour = '0' + sHour
    while len(sMin) < 2:
        sMin = '0' + sMin
    while len(sSec) < 2:
        sSec = '0' + sSec
    print(sHour +':'+ sMin +':'+ sSec)

def solve2():
    currentTime = input().split(':')
    cHour = int(currentTime[0]) 
    cMin = int(currentTime[1]) 
    cSec = int(currentTime[2]) 

    explosionTime = input().split(':')
    eHour = int(explosionTime[0]) 
    eMin = int(explosionTime[1]) 
    eSec = int(explosionTime[2])

    sHour = 0
    sMin = 0
    sSec = 0
    if eSec < cSec:
        sSec = (60-cSec)+eSec
        sMin -= 1
    else:
        sSec = eSec-cSec

    if eMin < cMin:
        sMin += (60-cMin)+eMin
        sHour -= 1
    else:
        sMin += eMin - cMin

    if eHour < cHour:
        sHour += (24-cHour)+eHour
    else:
        sHour += eHour-cHour

    if sMin < 0:
        sMin = 59
        sHour -= 1
    if sHour == 0 and sMin == 0 and sSec == 0: # was missing this edge case before
        sHour = 24
    sHour = str(sHour)
    sMin = str(sMin)
    sSec = str(sSec)
    while len(sHour) < 2:
        sHour = '0' + sHour
    while len(sMin) < 2:
        sMin = '0' + sMin
    while len(sSec) < 2:
        sSec = '0' + sSec
    print(sHour +':'+ sMin +':'+ sSec)


def main():
    #solve1()
    solve2()
main()