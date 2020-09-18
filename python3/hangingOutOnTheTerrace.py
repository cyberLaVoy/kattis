
params = input().split()

limit = int(params[0])
numEvents = int(params[1])

current = 0
denied = 0
for i in range(numEvents):
    event = input().split()
    event[1] = int(event[1])
    if event[0] == "enter":
        if current + event[1] > limit:
            denied += 1
        else:
            current += event[1]
    else:
        current -= event[1]
print(denied)
