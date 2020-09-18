
def pieceType(piece):
    typeOrder = ["K", "Q", "R", "B", "N", "P"]
    return typeOrder.index(piece[0])
def rowNumber(piece):
    return int(piece[2])
def columnLabel(piece):
    return piece[1]

def isUpper(l):
    return ord(l) <= 90 and ord(l) >= 65

def classifyPieces(board):
    pieces = {"Black": [], "White": []}
    for i in range(len(board)):
        for j in range(len(board[i])):
            piece = board[i][j]
            if piece not in ".:": 
                description = piece.upper() + chr(j+97) + str(8-i)
                if isUpper(piece):
                    pieces["White"].append(description)
                else:
                    pieces["Black"].append(description)
    return pieces


def sortPieces(pieces):
    pieces["Black"].sort(key=columnLabel)
    pieces["Black"].sort(key=rowNumber, reverse=True)
    pieces["Black"].sort(key=pieceType)

    pieces["White"].sort(key=columnLabel)
    pieces["White"].sort(key=rowNumber)
    pieces["White"].sort(key=pieceType)

def printPieces(pieces):
    print("White:", ','.join([x.replace('P', '') for x in pieces["White"]]))
    print("Black:", ','.join([x.replace('P', '') for x in pieces["Black"]]))

def main():
    board = []
    for i in range(17):
        if i & 1 == 1:
            row = [x[1] for x in input().split('|')[1:-1]]
            board.append(row)
        else:
            input()
    pieces = classifyPieces(board)
    sortPieces(pieces)
    printPieces(pieces)
main()