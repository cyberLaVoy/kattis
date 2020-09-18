

def isCorrect(board):
    is_correct = True
    for row in board:
        if "WWW" in row or "BBB" in row:
            is_correct = False
        blackCount = 0
        whiteCount = 0
        for l in row:
            if l == "W":
                whiteCount += 1
            else:
                blackCount += 1
        if blackCount != whiteCount:
            is_correct = False
    for j in range(len(board[0])):
        blackCount = 0
        whiteCount = 0
        col = ""
        for i in range(len(board)):
            col += board[i][j]
            if board[i][j] == "W":
                whiteCount += 1
            else:
                blackCount += 1
        if "WWW" in col or "BBB" in col:
            is_correct = False
        if blackCount != whiteCount:
            is_correct = False
    return int(is_correct)
        
    

def main():
    size = int(input())
    board = []
    for _ in range(size):
        line = input()
        board.append(line)
    print( isCorrect(board) )
main()