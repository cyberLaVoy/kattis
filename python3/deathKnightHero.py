
numBattles = int(input())

won = 0
for i in range(numBattles):
    battle = input()
    gameWon = True
    if "CD" in battle:
        gameWon = False
    if gameWon:
        won += 1
print(won)
