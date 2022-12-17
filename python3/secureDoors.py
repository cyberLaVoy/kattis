
numActions = int(input())

actions = {}
for i in range(numActions):
    action = input().split()
    person = action[1]
    move = action[0]
    anomaly = False
    if person in actions:
        if actions[person] == move:
            anomaly = True
    else:
        if move == "exit":
            anomaly = True
    actions[person] = move
    string = person
    if move == "entry":
        string += " entered"
    else:
        string += " exited"
    if anomaly:
        string += " (ANOMALY)"
    print(string)
            
