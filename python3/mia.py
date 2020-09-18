
def isMia(pair):
    return 1 in pair and 2 in pair
def isDouble(pair):
    return pair[0] == pair[1]
def combo(pair):
    tempPair = pair[:]
    tempPair.sort()
    return tempPair.pop()*10 + tempPair.pop()

def whoWins(pair1, pair2):
    player1 = "Player 1 wins."
    player2 = "Player 2 wins."
    tie = "Tie."
    combo1 = combo(pair1)
    combo2 = combo(pair2)
    if isMia(pair1) and isMia(pair2):
        return tie
    elif isMia(pair1):
        return player1
    elif isMia(pair2):
        return player2

    elif isDouble(pair1) and isDouble(pair2):
        if combo1 > combo2:
            return player1
        elif combo2 > combo1:
            return player2
        else:
            return tie
    elif isDouble(pair1):
        return player1
    elif isDouble(pair2):
        return player2

    else:
        if combo1 > combo2:
            return player1
        elif combo2 > combo1:
            return player2
        else:
            return tie


def solve():
    dice = input().split()
    dice = [int(x) for x in dice]
    while 0 not in dice:
        pair1 = dice[0:2]
        pair2 = dice[2:]
        print(whoWins(pair1, pair2))
            
        dice = input().split()
        dice = [int(x) for x in dice]
solve()
