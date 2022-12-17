ranks = {'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0}

hand = input().split(' ')

strength = 0
for card in hand:
    ranks[card[0]] += 1
    rankScore = ranks[card[0]]
    if rankScore > strength:
        strength = rankScore

print(strength)


