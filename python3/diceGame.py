import math 

def possibilityCount(dice):
    possibilityCount = {}
    low1 = dice[0]
    low2 = dice[2]
    high1 = dice[1]
    high2 = dice[3]
    for i in range(low1, high1+1):
        for j in range(low2, high2+1):
            if i+j not in possibilityCount:
                possibilityCount[i+j] = 1
            else:
                possibilityCount[i+j] += 1
    return possibilityCount

def E(possibilityCount):
    E = 0
    totalPossible = 0
    for possibility in possibilityCount:
        totalPossible += possibilityCount[possibility]
    for possibility in possibilityCount:
        E += possibility*possibilityCount[possibility]/totalPossible
    return round(E,7)

def solve():
    gunnarDice = input().split()
    gunnarDice = [int(x) for x in gunnarDice]
    emmaDice = input().split()
    emmaDice = [int(x) for x in emmaDice]
    gunnerPossCount = possibilityCount(gunnarDice)
    emmaPossCount = possibilityCount(emmaDice)
    gunnerE = E(gunnerPossCount)
    emmaE = E(emmaPossCount)
    if gunnerE > emmaE:
        print("Gunnar")
    elif emmaE > gunnerE:
        print("Emma")
    else:
        print("Tie")
solve()