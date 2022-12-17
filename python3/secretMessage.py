import math

def makeSecret(message):
    squareSize = len(message)
    squareSize = math.ceil(math.sqrt(squareSize))
    padding = '*'*(squareSize**2-len(message))
    message += padding
    square = []
    for i in range(squareSize):
        row = []
        for j in range(squareSize):
            letter = message[i*squareSize+j]
            row.append(letter)
        square.append(row)
    secret = ""
    for j in range(squareSize):
        for i in range(squareSize-1,-1,-1):
            letter = square[i][j]
            if letter != '*':
                secret += letter
    return secret

def solve():
    numMessages = int(input())
    for i in range(numMessages):
        message = input()
        print(makeSecret(message))
solve()