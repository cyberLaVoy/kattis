
vCards = ["Estate", "Duchy", "Province"]
vCost = [2,5,8]
tCards = ["Copper", "Silver", "Gold"]
tCost = [0,3,6]
cards = input().split()

G = int(cards[0])
S = int(cards[1])
C = int(cards[2])

value = G*3+S*2+C

bestTreasure = ""
for i in range(len(tCost)):
    if tCost[i] <= value: 
        bestTreasure = tCards[i]

bestVictory = ""
for i in range(len(vCost)):
    if vCost[i] <= value: 
        bestVictory = vCards[i] + " or "

print(bestVictory, bestTreasure, sep='')
    
