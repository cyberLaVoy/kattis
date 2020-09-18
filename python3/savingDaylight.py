import sys

params = sys.stdin.readline().strip()
while params != '':
    params = params.split()
    riseTime = params[-2].split(':')
    setTime = params[-1].split(':')
    riseTime = [int(x) for x in riseTime]
    setTime = [int(x) for x in setTime]
    hours = setTime[0]-riseTime[0]
    minutes = setTime[1]-riseTime[1]
    if minutes < 0:
        hours -= 1
        minutes = 60 + minutes
    print(params[0], params[1], params[2], hours, "hours", minutes, "minutes")
    
    params = sys.stdin.readline().strip()