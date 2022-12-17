import sys
sys.setrecursionlimit(1000000)

def countStars(image, numRows, numCols):
    numStars = 0
    for i in range(numRows):
        for j in range(numCols):
            if image[i][j] == '-':
                numStars += 1
                fill(image, i, j)
    return numStars

def fill(image, row, column):
    image[row][column] = '#'
    if row-1 >= 0:
        if image[row-1][column] == '-':
            fill(image, row-1, column)
    if row+1 < len(image):
        if image[row+1][column] == '-':
            fill(image, row+1, column)
    if column-1 >= 0:
        if image[row][column-1] == '-':
            fill(image, row, column-1)
    if column+1 < len(image[row]):
        if image[row][column+1] == '-':
            fill(image, row, column+1)

def solve():
    case = 0
    for line in sys.stdin:
        case += 1
        specs = line.split(' ')
        numRows = int(specs[0])
        numCols = int(specs[1])
        image = []
        for i in range(numRows):
            row = input()
            row = [pixel for pixel in row]
            image.append(row)
        numStars = countStars(image,numRows,numCols)
        print("Case", str(case)+':', numStars)
solve()
