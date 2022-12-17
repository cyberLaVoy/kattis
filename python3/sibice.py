import math

situation = input().split(' ')

numMatches = int(situation[0])
boxWidth = int(situation[1])
boxHeight = int(situation[2])

hypotenuse = math.sqrt(boxWidth**2 + boxHeight**2)

for i in range(numMatches):
    matchLength = int(input())
    if matchLength <= hypotenuse:
        print("DA")
    else:
        print("NE")