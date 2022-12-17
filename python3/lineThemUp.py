
numPlayers = int(input())

players = []
for i in range(numPlayers):
    player = input()
    players.append(player)

playersS = players[:]
playersRS = players[:]

playersS.sort()
playersRS.sort(reverse=True)

if players == playersS:
    print("INCREASING")
elif players == playersRS:
    print("DECREASING")
else:
    print("NEITHER")