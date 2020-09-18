

board = []
boardMeta = []
words = []

def search():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '#':
                if not boardMeta[i][j]["right"]:
                    word = searchRight(i,j)
                    if len(word) > 1:
                        words.append(word)
                if not boardMeta[i][j]["down"]:
                    word = searchDown(i,j)
                    if len(word) > 1:
                        words.append(word)

def searchRight(row, col):
    if col >= len(board[0]) or board[row][col] == '#':
        return ''
    boardMeta[row][col]["right"] = True
    return board[row][col] + searchRight(row, col+1)
def searchDown(row, col):
    if row >= len(board) or board[row][col] == '#':
        return ''
    boardMeta[row][col]["down"] = True
    return board[row][col] + searchDown(row+1, col)

def solve():
    dimensions = input().split()
    numRows = int(dimensions[0])
    for i in range(numRows):
        row = input()
        boardRow = []
        boardMetaRow = []
        for l in row:
            boardRow.append(l)
            boardMetaRow.append({"right": False, "down": False})
        board.append(boardRow)
        boardMeta.append(boardMetaRow)
    search()
    words.sort()
    print(words[0])
solve()   
