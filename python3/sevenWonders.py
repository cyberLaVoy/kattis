

cardsPlayed = input()
cardCounts = {}
for card in cardsPlayed:
    if card in cardCounts:
        cardCounts[card] += 1
    else:
        cardCounts[card] = 1

totalPoints = 0
for card in cardCounts:
    totalPoints += cardCounts[card]**2

if len(cardCounts) == 3:
    totalPoints += 7*cardCounts[min(cardCounts, key=cardCounts.get)]
print(totalPoints)