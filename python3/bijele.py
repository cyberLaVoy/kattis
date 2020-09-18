"""
One king
One queen
Two rooks
Two bishops
Two knights
Eight pawns
"""

perfectSet = [1,1,2,2,2,8]
currentSet = []

tally = input().split(' ')
tally = [int(x) for x in tally]

for i in range(6):
    currentSet.append(tally[i])

for j in range(6):
    print(perfectSet[j] - currentSet[j], end=' ')
print()
