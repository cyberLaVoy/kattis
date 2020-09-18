
params = input().split()
syllables = int(params[0])
numPlayers = int(params[1])


players = [ (i, "closed") for i in range(1, numPlayers+1) ]

position = 0

while len(players) > 1:
    position = (position + syllables-1) % len(players)
    player = players[position][0]
    status = players[position][1]
    if status == "closed":
        players = players[:position] + [(player, "open"), (player, "open")] + players[position+1:]
    if status == "open":
        players = players[:position] + [(player, "spilt")] + players[position+1:]
        position += 1
    if status == "spilt":
        players = players[:position] + players[position+1:]

print(players[0][0])

