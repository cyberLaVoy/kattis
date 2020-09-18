
pointsTable = {'A':(11,11), 'K':(4,4), 'Q':(3,3), 'J':(20, 2), 'T':(10, 10), '9':(14, 0), '8':(0,0), '7':(0,0)}

header = input().split(' ')

numHands = int(header[0])
dominantSuit = header[1]

totalPoints = 0
for i in range(4*numHands):
    card = input()
    cardNumber = card[0]
    cardSuit = card[1]
    if cardSuit == dominantSuit: 
        totalPoints += pointsTable[cardNumber][0]
    else:
        totalPoints += pointsTable[cardNumber][1]

print(totalPoints)
    
