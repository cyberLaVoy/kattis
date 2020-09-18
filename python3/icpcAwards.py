
numTeams = int(input())

teams = {}
for i in range(numTeams):
    team = input().split()
    if team[0] not in teams:
        teams[team[0]] = "found"
        print(team[0], team[1])
    if len(teams) == 12:
        break
