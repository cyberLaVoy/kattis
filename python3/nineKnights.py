
def valid(row, col):
    if row < 0 or col < 0:
        return False
    if row > 4 or col > 4:
        return False
    return True

def setPossibleMoves(mask,  i, j):
    moves = [[1,2],[1,-2],[-1,2], [-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    for move in moves:
        row = i + move[0]
        col = j + move[1]
        if valid(row, col):
            mask[row][col] = 1

def isValidLayout(board, mask):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'k' and mask[i][j] == 1:
                return False
    return True

def solve():
    board = []
    mask = []
    for i in range(5):
        row = input()
        row = [l for l in row]
        maskRow = [0]*5
        board.append(row)
        mask.append(maskRow)

    totalKnights = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'k':
                totalKnights += 1
                setPossibleMoves(mask, i,j)

    if isValidLayout(board, mask) and totalKnights == 9:
        print("valid")
    else:
        print("invalid")

solve()