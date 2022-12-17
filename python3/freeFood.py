
numEvents = int(input())

eventDays = [False]*366
for i in range(numEvents):
    event = input().split()
    event = [int(x) for x in event]
    for j in range(event[0], event[1]+1):
        eventDays[j] = True

totalDays = 0
for i in range(len(eventDays)):
    if eventDays[i]:
        totalDays += 1
print(totalDays)


