
numObs = int(input())

actualSeconds = 0
SLSeconds = 0
for i in range(numObs):
    observation = input().split()
    M = int(observation[0])
    S = int(observation[1])
    actualSeconds += 60*M
    SLSeconds += S
ratio = SLSeconds/actualSeconds 
if ratio > 1:
    print(ratio)
else:
    print("measurement error")