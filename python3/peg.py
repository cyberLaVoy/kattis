

def transposeBoard(board):
    transposed = []
    for _ in range(7):
        transposed.append("")
    for j in range(7):
        for i in range(7):
            transposed[i] += board[j][i]
    return transposed

def countLegalMovesIN(board):
    moveCount = 0
    legalMoves = ["oo.", ".oo"]
    for row in board:
        i, j = 0, 3
        while j <= len(row):
            if row[i:j] in legalMoves:
                moveCount += 1
            i += 1
            j += 1
    return moveCount

def countLegalMoves(board):
    moveCount = countLegalMovesIN(board)
    moveCount += countLegalMovesIN(transposeBoard(board))
    return moveCount


def main():
    board = []
    for _ in range(7):
        #board.append([str(x) for x in input()])
        board.append(input())
    moveCount = countLegalMoves(board)
    print(moveCount)


if __name__ == "__main__":
    main()