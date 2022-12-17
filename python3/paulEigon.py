import math

params = input().split()

turn = int(params[0])
gamesPlayed = int(params[1]) + int(params[2])

serve = math.floor(gamesPlayed/turn)

if serve & 1 == 0:
    print("paul")
else:
    print("opponent")
