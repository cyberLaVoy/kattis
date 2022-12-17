
votes = {}
name = input()
while name != "***":
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    name = input()

maximumVote = max(votes.values())
winningNames = []
for name in votes:
    if votes[name] == maximumVote:
        winningNames.append(name)
if len(winningNames) == 1:
    print(winningNames[0])
else:
    print("Runoff!")
