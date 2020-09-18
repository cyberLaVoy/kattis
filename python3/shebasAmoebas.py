
def eraseAmoeba(dish, row, col):
    dish[row][col] = '.'
    if row + 1 < len(dish):
        if dish[row+1][col] == '#':
            eraseAmoeba(dish, row+1, col)
    if row - 1 >= 0:
        if dish[row-1][col] == '#':
            eraseAmoeba(dish, row-1, col)

    if col + 1 < len(dish[row]):
        if dish[row][col+1] == '#':
            eraseAmoeba(dish, row, col+1)
        if row + 1 < len(dish):
            if dish[row+1][col+1] == '#':
                eraseAmoeba(dish, row+1, col+1)
        if row - 1 >= 0:
            if dish[row-1][col+1] == '#':
                eraseAmoeba(dish, row-1, col+1)

    if col - 1 >= 0:
        if dish[row][col-1] == '#':
            eraseAmoeba(dish, row, col-1)
        if row + 1 < len(dish):
            if dish[row+1][col-1] == '#':
                eraseAmoeba(dish, row+1, col-1)
        if row - 1 >= 0:
            if dish[row-1][col-1] == '#':
                eraseAmoeba(dish, row-1, col-1)

def numberOfAmoebas(dish):
    numAmoebas = 0
    for i in range(len(dish)):
        for j in range(len(dish[i])):
            if dish[i][j] == '#':
                numAmoebas += 1
                eraseAmoeba(dish, i, j)
    return numAmoebas

def solve():
    dimensions = input().split()
    numRows = int(dimensions[0])

    dish = []
    for i in range(numRows):
        row = input()
        row = [l for l in row]
        dish.append(row)
    print(numberOfAmoebas(dish))
solve()