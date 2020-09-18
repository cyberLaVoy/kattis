
attempt = input().split()
attempt[0] = int(attempt[0])
attempts = {}
while attempt[0] != -1:
    if attempt[1] not in attempts:
        attempts[attempt[1]] = {"solved": False, "failedAttempts": 0}
    if attempt[2] == "right":
        attempts[attempt[1]]["solved"] = True
        attempts[attempt[1]]["solvedTime"] = attempt[0]
    else:
        attempts[attempt[1]]["failedAttempts"] += 1
    attempt = input().split()
    attempt[0] = int(attempt[0])

solved = 0
time = 0
for attempt in attempts:
    if attempts[attempt]["solved"]:
        solved += 1
        time += attempts[attempt]["solvedTime"] + 20*attempts[attempt]["failedAttempts"]

print(solved, time)

