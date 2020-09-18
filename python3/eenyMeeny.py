

def printTeam(team):
    print(len(team))
    for member in team:
        print(member)

def main():
    syl = len(input().split())

    n = int(input())
    names = []

    for i in range(n):
        names.append(input())

    team1 = []
    team2 = []

    team = 1
    spot = 0
    while len(names) > 0:
        spot = ( spot + syl-1 ) % len(names)
        if team == 1:
            team1.append(names[spot])
            team = 2
        else:
            team2.append(names[spot])
            team = 1
        names = names[0:spot] + names[spot+1:]

    printTeam(team1)
    printTeam(team2)

main()

